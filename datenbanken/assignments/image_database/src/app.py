import streamlit as st
import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from utils.model import load_model, get_image_embedding
from utils.db import insert_image, search_images_by_tags, get_all_images_with_embeddings

def save_image_to_db(model, file_obj, tags_string):
    try:
        # save image blob
        file_obj.seek(0) 
        bytes_data = file_obj.read()
        filename = file_obj.name

        
        # calculate embedding
        file_obj.seek(0) 
        embedding_list = get_image_embedding(model, file_obj)
        embedding_json = json.dumps(embedding_list)

        # insert into database
        insert_image(filename, bytes_data, embedding_json, tags_string)
            
        return True, f"Image '{filename}' successfully saved!"
        
    except Exception as e:
        return False, str(e)


def search_images_in_db(tags_string):
    search_list = [t.strip().lower() for t in tags_string.split(',') if t.strip()]
    if not search_list:
        return []

    return search_images_by_tags(search_list)


def search_similar_images(query_image_file, top_k=3):
    """Sucht ähnliche Bilder basierend auf Vektor-Ähnlichkeit."""
    
    # calculate embedding for the query image
    query_embedding = get_image_embedding(model, query_image_file)
    
    # get all images with embeddings
    rows = get_all_images_with_embeddings()
    
    if not rows:
        return []

    # calculate similarities
    db_ids = []
    db_vectors = []
    db_images = {} 
    
    for r in rows:
        img_id, fname, data, emb_json = r
        db_ids.append(img_id)
        db_vectors.append(emb_json) 
        db_images[img_id] = (fname, data)
        
    # transform JSON embeddings back to numpy arrays for similarity calculation
    query_vec_np = np.array([query_embedding])
    db_vecs_np = np.array(db_vectors)
    
    # calculate cosine similarities
    similarities = cosine_similarity(query_vec_np, db_vecs_np)[0]
    
    # get top_k most similar images
    best_indices = similarities.argsort()[::-1][:top_k]
    
    threshold = 0.5 # threshold for similarity
    results = []
    for idx in best_indices:
        score = similarities[idx]
        if score > threshold:   
            img_id = db_ids[idx]
            fname, data = db_images[img_id]
            results.append((fname, data, score))
            
    return results


if __name__ == "__main__":
    model = load_model()

    # app layout
    st.set_page_config(layout="centered")
    #st.title("")

    # control panel for mode selection
    selected_mode = st.segmented_control(
        "select mode",
        options=["upload", "tag search", "reverse search"],
        selection_mode="single",
        default="upload",
        label_visibility="collapsed"
    )

    if selected_mode == "upload":
        st.header("upload image")
        
        uploaded_file = st.file_uploader("choose image (png, jpg, jpeg)", type=['png', 'jpg', 'jpeg'])
        tags_input = st.text_input("enter tags for the image (comma separated):")
        
        if st.button("save image to database"):
            if uploaded_file is not None and tags_input:
                success, message = save_image_to_db(model, uploaded_file, tags_input)
                if success:
                    st.success(message)
                else:
                    st.error(f"error: {message}")
            else:
                st.warning("please enter an image and at least one tag to save")

    elif selected_mode == "reverse search":
        st.header("reverse image search")
        st.info("upload image to find similar images in the database")
        
        ai_upload = st.file_uploader("upload image to reverse search", type=['png', 'jpg', 'jpeg'])
        
        if ai_upload and st.button("start reverse search"):
            with st.spinner("searching for similar images..."):
                results = search_similar_images(ai_upload)
                
            if results:
                st.success(f"{len(results)} similar images found:")
                
                # show results in columns
                cols = st.columns(len(results))
                for idx, (filename, image_bytes, score) in enumerate(results):
                    with cols[idx]:
                        st.image(bytes(image_bytes), caption=f"{filename}\nsimilarity: {score:.1%}")
            else:
                st.warning("no images found similar to the uploaded image")


    else:
        # tag search mode
        st.header("search")
        
        search_input = st.text_input("enter tags to search (comma separated):")
        
        if st.button("search"):
            if search_input:
                results = search_images_in_db(search_input)
                
                if results:
                    st.success(f"{len(results)} images found with the given tags:")

                    # show results
                    for filename, image_bytes in results:
                        st.image(bytes(image_bytes), caption=filename, width=300)
                else:
                    st.info("no images found with the given tags")
            else:
                st.warning("enter at least one tag to search")

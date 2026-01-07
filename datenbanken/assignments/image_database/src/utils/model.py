import streamlit as st
from sentence_transformers import SentenceTransformer
from PIL import Image

# load and cache the model
@st.cache_resource
def load_model():
    return SentenceTransformer('clip-ViT-B-32')

def get_image_embedding(model, image_file):
    # convert file to PIL Image for the model
    img = Image.open(image_file)

    # get embedding
    embedding = model.encode(img)

    # return as list for JSON serialization
    return embedding.tolist() 

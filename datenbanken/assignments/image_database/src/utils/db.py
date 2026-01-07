import psycopg2

HOST = "localhost"
HOST = "postgres"
PORT = 5432
USER = "postgres"
DB_NAME = "image_db"
PASSWORD = "test1234"

DB_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

def insert_image(filename, bytes_data, embedding_json, tags_string):
    conn = psycopg2.connect(DB_URI)
    c = conn.cursor()

    try:

        # insert image
        c.execute("""
            INSERT INTO images (filename, image_data, embedding) 
            VALUES (%s, %s, %s) 
            RETURNING id
        """, (filename, bytes_data, embedding_json))        

        # get image id
        new_image_id = c.fetchone()[0]
        

        # save tags and links
        tag_list = [t.strip().lower() for t in tags_string.split(',') if t.strip()]
        
        for tag_val in tag_list:
            c.execute("""
                INSERT INTO tags (name) 
                VALUES (%s) 
                ON CONFLICT (name) DO NOTHING
            """, (tag_val,))
            
            # get tag id
            c.execute("SELECT id FROM tags WHERE name = %s", (tag_val,))
            tag_id = c.fetchone()[0]
            
            # link image and tag
            c.execute("""
                INSERT INTO image_tags (image_id, tag_id) 
                VALUES (%s, %s) 
                ON CONFLICT DO NOTHING
            """, (new_image_id, tag_id))
    except Exception:
        conn.rollback() 
    finally:
        c.close()
        conn.close()


def search_images_by_tags(search_list):
    conn = psycopg2.connect(DB_URI)
    c = conn.cursor()

    # get the search tags
    search_tags = ','.join(['%s'] * len(search_list))

    # SQL query to find images matching all tags
    try: 
        sql = f'''
            SELECT i.filename, i.image_data
            FROM images i
            JOIN image_tags it ON i.id = it.image_id
            JOIN tags t ON it.tag_id = t.id
            WHERE t.name IN ({search_tags})
            GROUP BY i.id, i.filename, i.image_data
            HAVING COUNT(DISTINCT t.id) = %s
        '''
        
        # generate params
        params = search_list + [len(search_list)]
        
        # query execution
        c.execute(sql, params)
        results = c.fetchall()
        
        c.close()
        conn.close()
        return results
    except Exception:
        conn.rollback()
        c.close()
        conn.close()
        return []   

def get_all_images_with_embeddings():
    conn = psycopg2.connect(DB_URI)
    c = conn.cursor()
    c.execute("SELECT id, filename, image_data, embedding FROM images WHERE embedding IS NOT NULL")
    rows = c.fetchall()
    conn.close()

    return rows

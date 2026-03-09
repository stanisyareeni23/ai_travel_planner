from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from groq import Groq
import os

API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key = API_KEY)
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

def load_chunks(text,source,chunk_size=200):
    chunks = []    
    start = 0
    while start < len(text) :
        end = start + chunk_size
        chunk_text = text[start:end]
        chunks.append({
            "text": chunk_text,
            "source": source,
        })
        start = end
    return chunks

def load_file(file):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()

def load_folders(folder_path):
    all_chunks = []
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path, file)
        text = load_file(file_path)
        chunks = load_chunks(text, file)
        all_chunks.extend(chunks)
    return all_chunks
       

def embedding(chunk):
    embedded_value = embed_model.encode(chunk)
    if len(embedded_value.shape)==1:
        embedded_value = embedded_value.reshape(1,-1)
    return embedded_value


def create_index(embedded_data):
    dim = embedded_data.shape[1]
    index = faiss.IndexFlatL2(dim) 
    index.add(np.array(embedded_data))
    return index

def search(chunks,query,index,top_k=2):
    query_embed = embed_model.encode(query)
    if len(query_embed.shape)==1:
        query_embed = query_embed.reshape(1,-1)
    distance, indices = index.search(np.array(query_embed),top_k)
    result = []
    for i in indices[0]:
        result.append(chunks[i])
    return result

def response(query,context):
    context_data = ""
    for data in context:
        context_data = context_data + data['text'] + "\n"
        context_data = context_data + data["source"] + "\n\n"
    prompt = f""" Give the answer only.
    Answer only from the following context
    context: {context_data}
    input: {query}
    """
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
        {
            "role": "user",
            "content": prompt
        }
        ],
    )
    return completion.choices[0].message.content

def pipeline(query):
    chunks = load_folders(r"D:\Project_Travel\ai_travel_planner\data")
    texts = [c["text"] for c in chunks]
    embed = embed_model.encode(texts)
    index = create_index(embed)
    search_data = search(chunks, query, index)
    output = response(query, search_data)
    return output
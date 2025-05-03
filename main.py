from fastapi import FastAPI, File, UploadFile
from sentence_transformers import SentenceTransformer
import faiss
import os
import uvicorn
from typing import List
import shutil

app = FastAPI()

# Pre-trained model for embeddings
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)

# FAISS index for similarity search
DIM = 384  # Embedding dimension for the model
index = faiss.IndexFlatL2(DIM)  # L2 distance
file_metadata = []  # Store file metadata (name, location, etc.)

# Directory to store uploaded files
UPLOAD_DIR = "uploaded_codebase"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_code(files: List[UploadFile]):
    """
    Upload a codebase and process it for indexing.
    """
    for file in files:
        file_location = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
        
        # Read and split the file into chunks (e.g., functions, classes)
        with open(file_location, "r", encoding="utf-8") as f:
            content = f.read()
            chunks = split_code(content)  # Implement a custom split_code() function
            
            # Create embeddings for each chunk and add to FAISS index
            embeddings = model.encode(chunks)
            index.add(embeddings)
            
            # Add metadata for retrieval
            for i, chunk in enumerate(chunks):
                file_metadata.append({
                    "chunk": chunk,
                    "file": file.filename,
                    "line_number": get_line_number(content, chunk)  # Implement line number mapping
                })
    
    return {"message": "Files uploaded and indexed successfully!"}

@app.get("/search/")
def search_code(query: str, top_k: int = 5):
    """
    Search the uploaded codebase with a natural language query.
    """
    query_embedding = model.encode([query])
    distances, indices = index.search(query_embedding, top_k)
    
    results = []
    for i in range(len(indices[0])):
        metadata = file_metadata[indices[0][i]]
        results.append({
            "chunk": metadata["chunk"],
            "file": metadata["file"],
            "line_number": metadata["line_number"],
            "distance": distances[0][i]
        })
    
    return {"query": query, "results": results}

def split_code(code: str):
    """
    Split the code into meaningful chunks (e.g., functions, classes).
    """
    # Basic splitting logic (can be improved with libraries like tree-sitter)
    return code.split("\n\n")  # Split by double newlines as a basic heuristic

def get_line_number(content: str, chunk: str):
    """
    Get the starting line number of a code chunk.
    """
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if chunk in "\n".join(lines[i:]):
            return i + 1
    return -1

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

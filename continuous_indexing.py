import os
import time

WATCH_DIR = "uploaded_codebase"

def watch_directory_and_reindex():
    """
    Watch a directory for new or updated files and re-index them.
    """
    file_timestamps = {}  # Track last modified times

    while True:
        for file_name in os.listdir(WATCH_DIR):
            file_path = os.path.join(WATCH_DIR, file_name)
            if not os.path.isfile(file_path):
                continue

            last_modified = os.path.getmtime(file_path)
            if file_name not in file_timestamps or file_timestamps[file_name] < last_modified:
                print(f"Re-indexing file: {file_name}")
                
                # Re-index the file
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    embeddings = model.encode(content)
                    index.add(embeddings)  # Add to FAISS index
                
                file_timestamps[file_name] = last_modified
        
        time.sleep(5)  # Check every 5 seconds

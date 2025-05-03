import filetype

# Map file extensions to programming languages
LANGUAGE_MAPPING = {
    ".py": "Python",
    ".java": "Java",
    ".js": "JavaScript",
    ".cs": "C#",
    ".cpp": "C++",
    ".rb": "Ruby",
}

# Function to detect file type
def detect_language(file_name):
    for ext, lang in LANGUAGE_MAPPING.items():
        if file_name.endswith(ext):
            return lang
    return "Unknown"

# Adjust embeddings based on language
def generate_language_specific_embeddings(file_name, content):
    language = detect_language(file_name)
    print(f"Processing file: {file_name} (Language: {language})")
    
    # Use a language-specific model if available
    if language in ["Python", "Java"]:
        model_name = "microsoft/codebert-base"  # Example language-specific model
    else:
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    
    model = SentenceTransformer(model_name)
    embeddings = model.encode(content)
    return embeddings

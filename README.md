# AI-Based-Code-Snippet-Searcher
This project is an AI-powered tool that allows users to upload large codebases and perform natural language queries to locate relevant code snippets. It leverages semantic search technologies for efficient and accurate results.
## Features
- **Natural Language Query**: Ask questions like "Where is the payment logic?" and find the relevant code instantly.
- **Multi-Language Support**: Works with multiple programming languages including Python, JavaScript, Java, and more.
- **Semantic Search**: Uses pre-trained Sentence Transformer models to understand the intent behind the query.
- **Efficient Indexing**: Stores embeddings in FAISS or ChromaDB for fast similarity searches.
- **Real-Time Updates**: Continuously monitors uploaded files for changes and re-indexes them.
- **Highlight Matches**: Highlights keywords in the search results to improve readability.
- **User Feedback**: Collects feedback to improve search accuracy over time.
- **Related Snippets**: Links related code snippets based on shared logic such as function calls or variables.

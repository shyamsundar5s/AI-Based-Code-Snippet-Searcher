from typing import List

def highlight_matches(code_chunk: str, query: str) -> str:
    """
    Highlight keywords from the query in the code chunk.
    """
    keywords = query.split()  # Split query into keywords
    highlighted_code = code_chunk
    for keyword in keywords:
        highlighted_code = highlighted_code.replace(
            keyword, f"<mark>{keyword}</mark>"
        )
    return highlighted_code

# Example usage
query = "payment logic"
code_chunk = "def payment_logic(amount, user):\n    # Process payment"
highlighted = highlight_matches(code_chunk, query)
print(highlighted)

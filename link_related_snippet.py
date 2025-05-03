from collections import defaultdict

# Example global mapping of related snippets
related_snippets = defaultdict(list)

def link_snippets(file_name: str, code_chunks: List[str]):
    """
    Link related code snippets based on shared variables or function calls.
    """
    for i, chunk in enumerate(code_chunks):
        for j, other_chunk in enumerate(code_chunks):
            if i != j and has_shared_logic(chunk, other_chunk):
                related_snippets[chunk].append(other_chunk)

def has_shared_logic(chunk1: str, chunk2: str) -> bool:
    """
    Determine if two code chunks share logic (e.g., variables or function calls).
    """
    keywords1 = set(chunk1.split())
    keywords2 = set(chunk2.split())
    return len(keywords1 & keywords2) > 0

# Example usage
code_chunks = [
    "def payment_logic(amount):",
    "class PaymentHandler:\n    def handle(self):\n        payment_logic(100)"
]
link_snippets("payment.py", code_chunks)
print(related_snippets)

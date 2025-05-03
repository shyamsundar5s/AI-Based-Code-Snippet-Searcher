from sentence_transformers import util

def suggest_query_refinements(original_query: str, codebase: List[str]):
    """
    Suggest refined queries to the user based on similarity to the codebase.
    """
    query_embedding = model.encode([original_query])
    code_embeddings = model.encode(codebase)

    # Find similar code snippets
    similarities = util.pytorch_cos_sim(query_embedding, code_embeddings)
    suggestions = [codebase[i] for i in similarities[0].argsort(descending=True)[:3]]
    return suggestions

# Example usage
original_query = "payment logic"
codebase = ["def payment_logic(amount):", "def refund_logic(amount):"]
refinements = suggest_query_refinements(original_query, codebase)
print("Suggestions:", refinements)

feedback_data = []  # Store feedback data

def collect_feedback(user_query: str, retrieved_snippets: List[str], feedback: str):
    """
    Collect feedback from the user for a given query and search results.
    """
    feedback_entry = {
        "query": user_query,
        "snippets": retrieved_snippets,
        "feedback": feedback  # E.g., "relevant" or "not relevant"
    }
    feedback_data.append(feedback_entry)
    print("Feedback collected:", feedback_entry)

# Example usage
user_query = "Where is the payment logic?"
retrieved_snippets = ["def payment_logic(amount):", "class PaymentHandler:"]
user_feedback = "relevant"
collect_feedback(user_query, retrieved_snippets, user_feedback)

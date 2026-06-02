from project.generation.rag_pipeline import (
    generate_answer
)

docs = [
    """
    Retrieval Augmented Generation
    combines retrieval systems with
    large language models.
    """
]

answer = generate_answer(
    "What is RAG?",
    docs
)

print(answer)
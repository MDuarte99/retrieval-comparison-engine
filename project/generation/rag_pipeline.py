from project.generation.ollama_client import (
    generate
)


def generate_answer(
    query,
    documents
):

    context = "\n\n".join(
        documents
    )

    prompt = f"""
You are an expert AI assistant.

Answer using ONLY the context below.

Context:

{context}

Question:

{query}

Answer:
"""

    return generate(
        prompt
    )
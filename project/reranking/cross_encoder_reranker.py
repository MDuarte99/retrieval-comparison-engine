from sentence_transformers import CrossEncoder

from project.config.settings import (
    RERANK_MODEL
)

model = CrossEncoder(
    RERANK_MODEL
)


def rerank(
    query,
    documents
):

    pairs = [
        [query, doc]
        for doc in documents
    ]

    scores = model.predict(
        pairs
    )

    ranked = sorted(
        zip(documents, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return ranked
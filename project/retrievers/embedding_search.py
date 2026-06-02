from sentence_transformers import (
    SentenceTransformer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

from project.config.settings import (
    EMBEDDING_MODEL
)

model = SentenceTransformer(
    EMBEDDING_MODEL
)


def embedding_search(
    query,
    chunks,
    embeddings
):

    query_embedding = model.encode(
        [query]
    )

    similarities = cosine_similarity(
        query_embedding,
        embeddings
    )[0]

    results = list(
        zip(
            chunks,
            similarities
        )
    )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results
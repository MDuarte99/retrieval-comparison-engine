import faiss
import numpy as np

from sentence_transformers import (
    SentenceTransformer
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

index = faiss.read_index(
    "project/data/processed/faiss.index"
)


def search(
    query,
    chunks,
    k=20
):

    query_embedding = model.encode(
        [query]
    )

    scores, indices = index.search(

        query_embedding.astype(
            np.float32
        ),

        k
    )

    results = []

    for score, idx in zip(

        scores[0],
        indices[0]
    ):

        results.append(

            (
                chunks[idx],
                float(score)
            )
        )

    return results
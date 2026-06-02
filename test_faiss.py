from project.data_loader import load_corpus

from project.vectorstore.faiss_search import (
    search
)

chunks, metadata, embeddings = (
    load_corpus()
)

results = search(
    "what is retrieval augmented generation",
    chunks,
    k=10
)

for rank, (doc, score) in enumerate(
    results,
    start=1
):

    print(f"\n#{rank}")
    print(f"Score: {score:.4f}")
    print(doc[:300])
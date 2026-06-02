from project.data_loader import load_corpus
from project.retrievers.bm25_search import bm25_search

chunks, metadata, embeddings = load_corpus()

results = bm25_search(
    "what is retrieval augmented generation",
    chunks
)

for i, (doc, score) in enumerate(results[:5], start=1):

    print(f"\n#{i}")
    print(f"Score: {score:.4f}")
    print(doc[:500])
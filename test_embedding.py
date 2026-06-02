# test_embedding.py

from project.data_loader import load_corpus
from project.retrievers.embedding_search import embedding_search

chunks, metadata, embeddings = load_corpus()

results = embedding_search(
    "what is retrieval augmented generation",
    chunks,
    embeddings
)

for i, (doc, score) in enumerate(results[:5], 1):

    print(f"\n#{i}")
    print(score)
    print(doc[:300])
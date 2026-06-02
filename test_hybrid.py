from project.data_loader import load_corpus

from project.retrievers.tfidf_search import tfidf_search
from project.retrievers.bm25_search import bm25_search
from project.retrievers.embedding_search import embedding_search

from project.fusion.weighted_fusion import weighted_fusion

chunks, metadata, embeddings = load_corpus()

query = "what is retrieval augmented generation"

tfidf_results = tfidf_search(
    query,
    chunks
)

bm25_results = bm25_search(
    query,
    chunks
)

embedding_results = embedding_search(
    query,
    chunks,
    embeddings
)

results = weighted_fusion(
    tfidf_results,
    bm25_results,
    embedding_results,
    chunks
)

for i, (doc, score) in enumerate(results[:10], start=1):

    print(f"\n#{i}")
    print(f"Score: {score:.4f}")
    print(doc[:500])
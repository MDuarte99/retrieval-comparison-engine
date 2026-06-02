tfidf_results
bm25_results
embedding_results

rrf_results = reciprocal_rank_fusion(
    [
        tfidf_results,
        bm25_results,
        embedding_results
    ]
)
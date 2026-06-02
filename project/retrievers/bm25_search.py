from rank_bm25 import BM25Okapi


def bm25_search(
    query,
    chunks
):

    tokenized_docs = [
        chunk.lower().split()
        for chunk in chunks
    ]

    bm25 = BM25Okapi(
        tokenized_docs
    )

    scores = bm25.get_scores(
        query.lower().split()
    )

    results = list(
        zip(chunks, scores)
    )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results
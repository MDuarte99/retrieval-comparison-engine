from project.config.settings import (
    TFIDF_WEIGHT,
    BM25_WEIGHT,
    EMBEDDING_WEIGHT
)


def normalize(score_dict):

    values = list(score_dict.values())

    minimum = min(values)
    maximum = max(values)

    return {
        doc: (
            score - minimum
        ) / (
            maximum - minimum + 1e-9
        )
        for doc, score in score_dict.items()
    }


def weighted_fusion(
    tfidf_results,
    bm25_results,
    embedding_results,
    chunks
):

    tfidf_dict = dict(tfidf_results)
    bm25_dict = dict(bm25_results)
    embedding_dict = dict(embedding_results)

    tfidf_dict = normalize(tfidf_dict)
    bm25_dict = normalize(bm25_dict)
    embedding_dict = normalize(embedding_dict)

    scores = {}

    for chunk in chunks:

        scores[chunk] = (
            TFIDF_WEIGHT * tfidf_dict.get(chunk, 0)
            + BM25_WEIGHT * bm25_dict.get(chunk, 0)
            + EMBEDDING_WEIGHT * embedding_dict.get(chunk, 0)
        )

    return sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )
from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)


def tfidf_search(
    query,
    chunks
):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    matrix = vectorizer.fit_transform(
        chunks
    )

    query_vector = vectorizer.transform(
        [query]
    )

    scores = cosine_similarity(
        query_vector,
        matrix
    )[0]

    results = list(
        zip(chunks, scores)
    )

    results.sort(
        key=lambda x: x[1],
        reverse=True
    )

    return results
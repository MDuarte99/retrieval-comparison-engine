def reciprocal_rank_fusion(
    rankings,
    k=60
):

    scores = {}

    for ranking in rankings:

        for rank, (doc, _) in enumerate(
            ranking,
            start=1
        ):

            scores[doc] = (
                scores.get(doc, 0)
                +
                1 / (k + rank)
            )

    return sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    )
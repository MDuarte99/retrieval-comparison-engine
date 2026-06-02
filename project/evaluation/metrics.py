import math


def recall_at_k(
    retrieved,
    relevant,
    k
):

    retrieved = retrieved[:k]

    hits = len(
        set(retrieved)
        &
        set(relevant)
    )

    return hits / len(relevant)


def mrr(
    retrieved,
    relevant
):

    for idx, doc in enumerate(
        retrieved,
        start=1
    ):

        if doc in relevant:

            return 1 / idx

    return 0


def ndcg_at_k(
    retrieved,
    relevant,
    k
):

    retrieved = retrieved[:k]

    dcg = 0

    for i, doc in enumerate(
        retrieved,
        start=1
    ):

        if doc in relevant:

            dcg += (
                1 /
                math.log2(i + 1)
            )

    ideal_hits = min(
        len(relevant),
        k
    )

    idcg = sum(
        1 / math.log2(i + 1)
        for i in range(
            1,
            ideal_hits + 1
        )
    )

    return (
        dcg / idcg
        if idcg > 0
        else 0
    )
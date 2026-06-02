from project.evaluation.metrics import (
    recall_at_k,
    mrr,
    ndcg_at_k
)


def evaluate(
    retrieved_docs,
    relevant_docs
):

    return {

        "Recall@5":
        recall_at_k(
            retrieved_docs,
            relevant_docs,
            5
        ),

        "Recall@10":
        recall_at_k(
            retrieved_docs,
            relevant_docs,
            10
        ),

        "MRR":
        mrr(
            retrieved_docs,
            relevant_docs
        ),

        "NDCG@10":
        ndcg_at_k(
            retrieved_docs,
            relevant_docs,
            10
        )
    }
from project.data_loader import load_corpus

from project.retrievers.tfidf_search import (
    tfidf_search
)

from project.retrievers.bm25_search import (
    bm25_search
)

from project.retrievers.embedding_search import (
    embedding_search
)

from project.vectorstore.faiss_search import (
    search as faiss_search
)

from project.fusion.reciprocal_rank_fusion import (
    reciprocal_rank_fusion
)

from project.reranking.cross_encoder_reranker import (
    rerank
)

from project.generation.rag_pipeline import (
    generate_answer
)


def print_results(
    title,
    results,
    top_k=5
):

    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)

    for rank, (doc, score) in enumerate(
        results[:top_k],
        start=1
    ):

        print(f"\n#{rank}")
        print(f"Score: {score:.4f}")
        print("-" * 80)

        preview = doc[:400]

        print(preview)

        if len(doc) > 400:
            print("...")


def run_pipeline(
    query,
    chunks,
    embeddings
):

    print("\nRunning TF-IDF Search...")

    tfidf_results = tfidf_search(
        query,
        chunks
    )

    print("Running BM25 Search...")

    bm25_results = bm25_search(
        query,
        chunks
    )

    print("Running Embedding Search...")

    embedding_results = embedding_search(
        query,
        chunks,
        embeddings
    )

    print("Running FAISS Search...")

    faiss_results = faiss_search(
        query,
        chunks,
        k=50
    )

    print("Applying Reciprocal Rank Fusion...")

    fused_results = reciprocal_rank_fusion(
        [
            tfidf_results,
            bm25_results,
            embedding_results,
            faiss_results
        ]
    )

    print_results(
        "HYBRID SEARCH RESULTS",
        fused_results,
        top_k=10
    )

    candidate_docs = [

        doc

        for doc, score

        in fused_results[:20]
    ]

    print("\nRunning Cross Encoder Reranking...")

    reranked_results = rerank(
        query,
        candidate_docs
    )

    print_results(
        "RERANKED RESULTS",
        reranked_results,
        top_k=10
    )

    final_context = [

        doc

        for doc, score

        in reranked_results[:5]
    ]

    print("\nGenerating Answer with Qwen3...")

    answer = generate_answer(
        query,
        final_context
    )

    return answer


def main():

    print("\nLoading corpus...")

    chunks, metadata, embeddings = (
        load_corpus()
    )

    print(
        f"Corpus loaded successfully."
    )

    print(
        f"Chunks: {len(chunks)}"
    )

    while True:

        query = input(
            "\nAsk a question (or type 'exit'): "
        ).strip()

        if query.lower() in [
            "exit",
            "quit",
            "q"
        ]:
            break

        answer = run_pipeline(
            query,
            chunks,
            embeddings
        )

        print("\n" + "=" * 80)
        print("RAG ANSWER")
        print("=" * 80)

        print(answer)

        print("\n")


if __name__ == "__main__":
    main()
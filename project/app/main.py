import os
import sys
from typing import List, Tuple

# =============================================================================
# BOOTSTRAP
# =============================================================================

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# =============================================================================
# IMPORTS
# =============================================================================

from project.data_loader import load_corpus
from project.retrievers.tfidf_search import tfidf_search
from project.retrievers.bm25_search import bm25_search
from project.retrievers.embedding_search import embedding_search
from project.vectorstore.faiss_search import search as faiss_search
from project.fusion.reciprocal_rank_fusion import reciprocal_rank_fusion
from project.reranking.cross_encoder_reranker import rerank
from project.generation.rag_pipeline import generate_answer

# =============================================================================
# CONFIGURATION
# =============================================================================

FAISS_K = 50
TOP_K_DISPLAY = 10
TOP_K_FUSION = 20
TOP_K_CONTEXT = 3

# =============================================================================
# UTILITIES
# =============================================================================


def log_step(message: str) -> None:
    """Display a standardized pipeline log message."""
    print(f"\n🔄 {message}")


def print_section(title: str) -> None:
    """Print section headers."""
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def print_results(
    title: str,
    results: List[Tuple[str, float]],
    top_k: int = TOP_K_DISPLAY
) -> None:
    """
    Display ranked search results.

    Args:
        title: Section title
        results: List of (document, score)
        top_k: Number of results to display
    """

    print_section(title)

    for rank, (doc, score) in enumerate(results[:top_k], start=1):
        print(f"\n#{rank}")
        print(f"Score: {score:.4f}")
        print("-" * 80)

        preview = doc[:400]
        print(preview)

        if len(doc) > 400:
            print("...")


# =============================================================================
# RETRIEVAL
# =============================================================================


def run_retrieval(
    query: str,
    chunks: List[str],
    embeddings
):
    """
    Execute all retrieval strategies and fuse results.
    """

    log_step("Running TF-IDF Search")
    tfidf_results = tfidf_search(query, chunks)

    log_step("Running BM25 Search")
    bm25_results = bm25_search(query, chunks)

    log_step("Running Embedding Search")
    embedding_results = embedding_search(
        query,
        chunks,
        embeddings
    )

    log_step("Running FAISS Search")
    faiss_results = faiss_search(
        query,
        chunks,
        k=FAISS_K
    )

    log_step("Applying Reciprocal Rank Fusion")

    fused_results = reciprocal_rank_fusion([
        tfidf_results,
        bm25_results,
        embedding_results,
        faiss_results
    ])

    print_results(
        "🔀 HYBRID SEARCH RESULTS",
        fused_results
    )

    return fused_results


# =============================================================================
# RERANKING
# =============================================================================


def run_reranking(
    query: str,
    fused_results
):
    """
    Execute Cross Encoder reranking.
    """

    candidate_docs = [
        doc
        for doc, _ in fused_results[:TOP_K_FUSION]
    ]

    print(
        f"\n📋 Selected {len(candidate_docs)} "
        f"candidates for reranking"
    )

    log_step("Running Cross Encoder Reranking")

    reranked_results = rerank(
        query,
        candidate_docs
    )

    print_results(
        "✨ RERANKED RESULTS",
        reranked_results
    )

    return reranked_results


# =============================================================================
# GENERATION
# =============================================================================


def run_generation(
    query: str,
    reranked_results
) -> str:
    """
    Generate final answer using RAG.
    """

    final_context = [
        doc
        for doc, _ in reranked_results[:TOP_K_CONTEXT]
    ]

    print(
        f"\n📚 Using {len(final_context)} "
        f"documents as generation context"
    )

    print("\n🤖 Generating Answer with Qwen3...")

    answer = generate_answer(
        query,
        final_context
    )

    return answer


# =============================================================================
# PIPELINE
# =============================================================================


def run_pipeline(
    query: str,
    chunks,
    embeddings
) -> str:
    """
    Execute the complete Hybrid Search + RAG workflow.
    """

    print_section(f"QUERY: {query}")

    fused_results = run_retrieval(
        query,
        chunks,
        embeddings
    )

    reranked_results = run_reranking(
        query,
        fused_results
    )

    answer = run_generation(
        query,
        reranked_results
    )

    return answer


# =============================================================================
# INTERACTIVE SESSION
# =============================================================================


def interactive_session(
    chunks,
    embeddings
) -> None:
    """
    Start CLI question-answering session.
    """

    print("\n" + "-" * 80)
    print("💡 System ready! Ask questions about your documents.")
    print("Type 'exit', 'quit', or 'q' to stop.")
    print("-" * 80)

    while True:

        query = input("\n❓ Ask a question: ").strip()

        if query.lower() in {"exit", "quit", "q"}:
            print("\n👋 Goodbye!")
            break

        if not query:
            print("⚠️ Please enter a valid question.")
            continue

        try:
            answer = run_pipeline(
                query,
                chunks,
                embeddings
            )

            print_section("💡 RAG ANSWER")
            print(answer)

        except Exception as exc:
            print(f"\n❌ Error processing query: {exc}")


# =============================================================================
# MAIN
# =============================================================================


def main() -> None:

    print_section(
        "🔍 HYBRID SEARCH ENGINE FOR TECHNICAL DOCUMENTATION"
    )

    print("\n📖 Loading corpus...")

    try:

        chunks, metadata, embeddings = load_corpus()

        print("\n✅ Corpus loaded successfully!")
        print(f"   - Total chunks: {len(chunks)}")

        if metadata:
            print("   - Metadata available: Yes")

        interactive_session(
            chunks,
            embeddings
        )

    except FileNotFoundError as exc:

        print("\n❌ Could not load corpus.")
        print(f"Details: {exc}")

        print("\n📁 Expected location:")
        print("project/data/raw/your_documents.txt")

    except Exception as exc:

        print(f"\n❌ Unexpected error: {exc}")


if __name__ == "__main__":
    main()
import sys
import os

# Add the project root directory to Python path
# This goes up 3 levels: from project/app/main.py to the project root
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, root_dir)

# Now imports work correctly
from project.data_loader import load_corpus
from project.retrievers.tfidf_search import tfidf_search
from project.retrievers.bm25_search import bm25_search
from project.retrievers.embedding_search import embedding_search
from project.vectorstore.faiss_search import search as faiss_search
from project.fusion.reciprocal_rank_fusion import reciprocal_rank_fusion
from project.reranking.cross_encoder_reranker import rerank
from project.generation.rag_pipeline import generate_answer


def print_results(title, results, top_k=5):
    """
    Print formatted search results
    
    Args:
        title: Section title
        results: List of tuples (document, score)
        top_k: Number of results to display
    """
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)
    
    for rank, (doc, score) in enumerate(results[:top_k], start=1):
        print(f"\n#{rank}")
        print(f"Score: {score:.4f}")
        print("-" * 80)
        
        preview = doc[:400]
        print(preview)
        
        if len(doc) > 400:
            print("...")


def run_pipeline(query, chunks, embeddings):
    """
    Execute the complete hybrid search pipeline
    
    Args:
        query: Query string
        chunks: List of document chunks
        embeddings: Embeddings matrix
    
    Returns:
        answer: Generated answer from RAG model
    """
    
    print("\n" + "=" * 80)
    print(f"QUERY: {query}")
    print("=" * 80)
    
    # 1. TF-IDF Search
    print("\n🔄 Running TF-IDF Search...")
    tfidf_results = tfidf_search(query, chunks)
    print(f"   ✓ Found {len(tfidf_results)} results")
    
    # 2. BM25 Search
    print("\n🔄 Running BM25 Search...")
    bm25_results = bm25_search(query, chunks)
    print(f"   ✓ Found {len(bm25_results)} results")
    
    # 3. Embedding Search
    print("\n🔄 Running Embedding Search...")
    embedding_results = embedding_search(query, chunks, embeddings)
    print(f"   ✓ Found {len(embedding_results)} results")
    
    # 4. FAISS Search
    print("\n🔄 Running FAISS Search...")
    faiss_results = faiss_search(query, chunks, k=50)
    print(f"   ✓ Found {len(faiss_results)} results")
    
    # 5. Reciprocal Rank Fusion
    print("\n🔗 Applying Reciprocal Rank Fusion...")
    fused_results = reciprocal_rank_fusion([
        tfidf_results,
        bm25_results,
        embedding_results,
        faiss_results
    ])
    print(f"   ✓ Combined {len(fused_results)} results")
    
    # 6. Display hybrid search results
    print_results("🔀 HYBRID SEARCH RESULTS", fused_results, top_k=10)
    
    # 7. Select candidates for reranking
    candidate_docs = [doc for doc, score in fused_results[:20]]
    print(f"\n📋 Selected {len(candidate_docs)} candidates for reranking")
    
    # 8. Cross-Encoder Reranking
    print("\n🎯 Running Cross Encoder Reranking...")
    reranked_results = rerank(query, candidate_docs)
    print(f"   ✓ Reranked {len(reranked_results)} results")
    
    # 9. Display reranked results
    print_results("✨ RERANKED RESULTS", reranked_results, top_k=10)
    
    # 10. Select final context
    final_context = [doc for doc, score in reranked_results[:5]]
    print(f"\n📚 Using {len(final_context)} documents as context for generation")
    
    # 11. Generate answer with RAG
    print("\n🤖 Generating Answer with Qwen3...")
    answer = generate_answer(query, final_context)
    
    return answer


def main():
    """
    Main function of the system
    """
    print("\n" + "=" * 80)
    print("🔍 HYBRID SEARCH ENGINE FOR TECHNICAL DOCUMENTATION")
    print("=" * 80)
    print("\n📖 Loading corpus...")
    
    try:
        # Load corpus and embeddings
        chunks, metadata, embeddings = load_corpus()
        
        print(f"\n✅ Corpus loaded successfully!")
        print(f"   - Total chunks: {len(chunks)}")
        
        if metadata:
            print(f"   - Metadata available: Yes")
        
        print("\n" + "-" * 80)
        print("💡 System ready! Ask questions about your documents.")
        print("   Type 'exit', 'quit', or 'q' to stop.")
        print("-" * 80)
        
        # Interactive loop
        while True:
            # Get user query
            query = input("\n❓ Ask a question: ").strip()
            
            # Check for exit condition
            if query.lower() in ["exit", "quit", "q"]:
                print("\n👋 Goodbye!")
                break
            
            # Check for empty query
            if not query:
                print("⚠️  Please enter a valid question.")
                continue
            
            # Execute pipeline
            try:
                answer = run_pipeline(query, chunks, embeddings)
                
                # Display final answer
                print("\n" + "=" * 80)
                print("💡 RAG ANSWER")
                print("=" * 80)
                print(answer)
                print("\n" + "=" * 80)
                
            except Exception as e:
                print(f"\n❌ Error processing query: {str(e)}")
                print("Please try again with a different question.")
                
    except FileNotFoundError as e:
        print(f"\n❌ Error: Could not load corpus.")
        print(f"   Details: {str(e)}")
        print("\n📁 Please ensure your documents are in the correct location:")
        print("   - project/data/raw/your_documents.txt")
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        print("Please check your installation and data files.")


if __name__ == "__main__":
    main()
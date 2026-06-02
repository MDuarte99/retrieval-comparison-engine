# 🔍 Hybrid Search Engine for Technical Documentation

🐍 Python 3.8+ | 📄 MIT License | ⚫ Code Style: Black

A production-ready hybrid search and RAG (Retrieval-Augmented Generation) system that combines multiple retrieval strategies for optimal document search and question answering.

---

## 🎯 Features

| Component | Description |
|----------|-------------|
| **Multi-Strategy Retrieval** | Lexical (TF-IDF, BM25) + Semantic (Embeddings, FAISS) |
| **Reciprocal Rank Fusion (RRF)** | Combines multiple ranking strategies intelligently |
| **Cross-Encoder Reranking** | Improves relevance using transformer-based reranking |
| **RAG Pipeline** | Generates answers using Qwen3 language model |
| **Scalable Architecture** | Modular design for easy extension and experimentation |

---

## 🏗️ Architecture
User Query
│
├─── Lexical Retrievers (TF-IDF, BM25)
├─── Semantic Retrievers (Embeddings, FAISS)
│
└─── Reciprocal Rank Fusion (RRF)
│
├─── Cross-Encoder Reranking
│
└─── RAG Generation (Qwen3)
│
└─── Final Answer




---

## 📦 Installation

### 1. Clone the Repository

### 2. Create Virtual Environment
# Using venv
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on Linux/Mac
source venv/bin/activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Set Up Data
project/data/raw/
└── your_documents.txt

###🚀 Usage
Run Pipeline
python main.py

### Interactive Q&A

from main import run_pipeline
from project.data_loader import load_corpus

chunks, metadata, embeddings = load_corpus()

answer = run_pipeline(
    "How does transformer architecture work?",
    chunks,
    embeddings
)

print(answer)


📊 Retrieval Strategies
1. TF-IDF Search
Term frequency-inverse document frequency
Fast keyword matching
Highly interpretable
2. BM25 Search
Probabilistic ranking model
Better document length normalization
Industry standard
3. Embedding Search
Semantic similarity using transformers
Handles synonyms and context
Strong generalization
4. FAISS Search
Efficient vector similarity search
Scalable to millions of documents
Optimized performance
🔄 Fusion & Reranking
Reciprocal Rank Fusion (RRF)
Combines multiple ranking signals
Reduces bias between retrievers
Improves overall ranking quality
Cross-Encoder Reranking
Joint query-document evaluation
Transformer-based scoring
Higher precision results
💡 RAG Pipeline
Retrieves relevant context
Uses Qwen3 for generation
Produces grounded answers based on documents
📁 Project Structure
Hybrid-Search-for-Technical-Documentation/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── project/
    ├── data_loader.py
    ├── retrievers/
    │   ├── tfidf_search.py
    │   ├── bm25_search.py
    │   └── embedding_search.py
    ├── vectorstore/
    │   └── faiss_search.py
    ├── fusion/
    │   └── reciprocal_rank_fusion.py
    ├── reranking/
    │   └── cross_encoder_reranker.py
    └── generation/
        └── rag_pipeline.py
🧪 Example Queries
query = "What are the main components of a transformer model?"

query = "How does BERT differ from GPT?"

query = "How do I implement attention mechanism in PyTorch?"
📈 Performance Features
Parallel retrieval execution
Cached embeddings and indices
FAISS scalable search (million-scale)
Fully configurable pipeline
🔧 Configuration
fused_results = reciprocal_rank_fusion(results, k=60)

reranked_results = rerank(query, candidate_docs, top_k=10)

faiss_results = faiss_search(query, chunks, k=50)
🐛 Troubleshooting
Issue	Solution
Memory errors	Reduce embedding batch size
Slow FAISS search	Lower k or use GPU
Missing dependencies	pip install -r requirements.txt
Model download fails	Check internet or cache
📝 Requirements
Python 3.8+
8GB+ RAM (16GB recommended)
GPU optional
~2GB disk space
🤝 Contributing
Fork repo
Create branch:
git checkout -b feature/amazing-feature
Commit:
git commit -m "Add amazing feature"
Push:
git push origin feature/amazing-feature
Open Pull Request
📄 License

MIT License

🙏 Acknowledgments
Sentence Transformers → https://www.sbert.net/
FAISS → https://github.com/facebookresearch/faiss
Qwen → https://github.com/QwenLM/Qwen
📧 Contact

Author: MDuarte99
Project: https://github.com/MDuarte99/Hybrid-Search-for-Technical-Documentation

⭐ If you like this project, give it a star!

```bash
git clone https://github.com/MDuarte99/Hybrid-Search-for-Technical-Documentation.git
cd Hybrid-Search-for-Technical-Documentation

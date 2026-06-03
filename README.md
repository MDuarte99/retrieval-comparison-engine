# 🔍 Hybrid Search Engine for Technical Documentation

Production-ready Hybrid Search and Retrieval-Augmented Generation (RAG) system for technical documentation. This project combines lexical retrieval, semantic search, rank fusion, reranking, and LLM-based answer generation to deliver highly relevant search results and grounded responses.

Built with modern Information Retrieval (IR) and Generative AI techniques, the system demonstrates how enterprise-grade search architectures combine multiple retrieval strategies to maximize recall and precision.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Code%20Style](https://img.shields.io/badge/Code%20Style-Black-black)

---

# 🚀 Key Features

| Feature                      | Description                                              |
| ---------------------------- | -------------------------------------------------------- |
| Multi-Strategy Retrieval     | Combines lexical and semantic retrieval approaches       |
| TF-IDF Search                | Fast keyword-based retrieval                             |
| BM25 Ranking                 | Industry-standard probabilistic ranking algorithm        |
| Embedding Search             | Semantic retrieval using transformer embeddings          |
| FAISS Vector Search          | Efficient similarity search at scale                     |
| Reciprocal Rank Fusion (RRF) | Merges rankings from multiple retrievers                 |
| Cross-Encoder Reranking      | Transformer-based relevance optimization                 |
| RAG Pipeline                 | Context-aware answer generation using Qwen3              |
| Modular Architecture         | Easily extensible for experimentation and production use |

---

# 🎯 Project Goals

The objective of this project is to demonstrate a modern retrieval pipeline capable of:

* Improving search relevance through hybrid retrieval
* Combining lexical and semantic understanding
* Enhancing ranking quality through reranking techniques
* Generating grounded answers from retrieved documentation
* Serving as a foundation for enterprise search systems and AI assistants

---

# 🏗️ System Architecture

```text
User Query
    │
    ├── TF-IDF Retrieval
    ├── BM25 Retrieval
    ├── Embedding Retrieval
    └── FAISS Vector Search
            │
            ▼
  Reciprocal Rank Fusion (RRF)
            │
            ▼
  Cross-Encoder Reranking
            │
            ▼
      Top Documents
            │
            ▼
      RAG Generation
        (Qwen3)
            │
            ▼
       Final Answer
```

---

# 🔄 Retrieval Pipeline

The retrieval workflow follows four stages:

### 1. Multi-Retriever Search

The query is processed by multiple retrieval systems:

* TF-IDF
* BM25
* Embedding Similarity Search
* FAISS Vector Search

Each retriever contributes unique strengths and ranking signals.

---

### 2. Rank Fusion

Results from all retrievers are merged using Reciprocal Rank Fusion (RRF).

Benefits:

* Increases recall
* Reduces retriever bias
* Produces more robust rankings

---

### 3. Reranking

A Cross-Encoder evaluates the query-document pairs jointly.

Benefits:

* Higher precision
* Improved relevance estimation
* Better final ranking quality

---

### 4. Answer Generation

The highest-ranked documents are passed to a Retrieval-Augmented Generation pipeline using Qwen3.

The model generates responses grounded in retrieved context, reducing hallucinations and improving factual accuracy.

---

# 📂 Project Structure

```text
Hybrid-Search-for-Technical-Documentation/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── project/
    │
    ├── data_loader.py
    │
    ├── retrievers/
    │   ├── tfidf_search.py
    │   ├── bm25_search.py
    │   └── embedding_search.py
    │
    ├── vectorstore/
    │   └── faiss_search.py
    │
    ├── fusion/
    │   └── reciprocal_rank_fusion.py
    │
    ├── reranking/
    │   └── cross_encoder_reranker.py
    │
    └── generation/
        └── rag_pipeline.py
```

---

# 📦 Installation

## Clone Repository

```bash
git clone https://github.com/MDuarte99/Hybrid-Search-for-Technical-Documentation.git

cd Hybrid-Search-for-Technical-Documentation
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

.\venv\Scripts\activate
```

### Linux / macOS

```bash
python -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📄 Data Setup

Place your documents inside:

```text
project/data/raw/
```

Example:

```text
project/data/raw/
└── technical_documentation.txt
```

---

# 🚀 Running the Pipeline

Execute:

```bash
python main.py
```

---

# 💬 Interactive Question Answering

```python
from main import run_pipeline
from project.data_loader import load_corpus

chunks, metadata, embeddings = load_corpus()

answer = run_pipeline(
    query="How does transformer architecture work?",
    chunks=chunks,
    embeddings=embeddings
)

print(answer)
```

---

# 🔎 Retrieval Methods

## TF-IDF

* Term Frequency-Inverse Document Frequency
* Fast keyword matching
* Highly interpretable

---

## BM25

* Probabilistic ranking model
* Length normalization
* Widely used in production search systems

---

## Embedding Search

* Transformer-based semantic search
* Handles synonyms and contextual meaning
* Strong generalization capabilities

---

## FAISS

* High-performance vector similarity search
* Scalable to millions of embeddings
* Optimized for large-scale retrieval

---

# 🔄 Fusion & Reranking

## Reciprocal Rank Fusion (RRF)

Combines rankings from multiple retrievers.

Advantages:

* Robust performance
* Improved recall
* Better ranking consistency

---

## Cross-Encoder Reranking

Uses transformer models to score query-document pairs.

Advantages:

* Context-aware scoring
* Higher precision
* Improved final ranking quality

---

# 🤖 Retrieval-Augmented Generation (RAG)

The generation layer:

1. Retrieves relevant documents
2. Builds contextual prompts
3. Uses Qwen3 for generation
4. Produces grounded responses

Benefits:

* Reduced hallucinations
* Improved factual consistency
* Better user experience

---

# 🧪 Example Queries

```python
"What are the main components of a transformer model?"
```

```python
"How does BERT differ from GPT?"
```

```python
"How do I implement attention mechanisms in PyTorch?"
```

```python
"What is Reciprocal Rank Fusion and why is it useful?"
```

---

# ⚡ Performance Features

* Parallel retrieval execution
* Cached embeddings
* FAISS indexing
* Configurable ranking pipeline
* Scalable architecture
* Modular experimentation framework

---

# 🔧 Configuration Examples

## Reciprocal Rank Fusion

```python
fused_results = reciprocal_rank_fusion(
    results,
    k=60
)
```

## Cross-Encoder Reranking

```python
reranked_results = rerank(
    query,
    candidate_docs,
    top_k=10
)
```

## FAISS Retrieval

```python
faiss_results = faiss_search(
    query,
    chunks,
    k=50
)
```

---

# 🐛 Troubleshooting

| Issue                   | Solution                             |
| ----------------------- | ------------------------------------ |
| Memory errors           | Reduce embedding batch size          |
| Slow retrieval          | Lower search depth (`k`)             |
| Missing dependencies    | Reinstall requirements               |
| Model download failures | Verify internet connection and cache |

---

# 📝 Requirements

### Minimum

* Python 3.8+
* 8GB RAM
* 2GB Free Disk Space

### Recommended

* Python 3.10+
* 16GB RAM
* CUDA-enabled GPU

---

# 🔮 Future Improvements

* Hybrid dense-sparse retrieval
* Query expansion
* Multi-vector retrieval
* Metadata filtering
* Streaming generation
* API deployment with FastAPI
* Evaluation metrics dashboard
* Agentic RAG workflows

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/amazing-feature
```

3. Commit your changes

```bash
git commit -m "Add amazing feature"
```

4. Push to GitHub

```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request

---

# 📄 License

Distributed under the MIT License.

---

# 🙏 Acknowledgments

* Sentence Transformers
* FAISS
* Qwen
* Hugging Face
* PyTorch

---

# 👨‍💻 Author

**Matheus Duarte**

GitHub:
https://github.com/MDuarte99

Project Repository:
https://github.com/MDuarte99/Hybrid-Search-for-Technical-Documentation

---

⭐ If you find this project useful, consider giving it a star.

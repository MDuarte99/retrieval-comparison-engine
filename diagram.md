## 🏗️ Architecture

```mermaid
flowchart TD

    A[User Query]

    A --> B[TF-IDF Search]
    A --> C[BM25 Search]
    A --> D[Embedding Search]
    A --> E[FAISS Vector Search]

    B --> F[Reciprocal Rank Fusion]
    C --> F
    D --> F
    E --> F

    F --> G[Cross-Encoder Reranking]

    G --> H[Top Relevant Documents]

    H --> I[Qwen3 RAG Generation]

    I --> J[Final Answer]
```
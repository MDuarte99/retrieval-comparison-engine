<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hybrid Search Engine for Technical Documentation</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
            line-height: 1.6;
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
            color: #24292e;
            background-color: #ffffff;
        }

        h1 {
            font-size: 2em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
            margin-bottom: 16px;
        }

        h2 {
            font-size: 1.5em;
            border-bottom: 1px solid #eaecef;
            padding-bottom: 0.3em;
            margin-top: 24px;
            margin-bottom: 16px;
        }

        h3 {
            font-size: 1.25em;
            margin-top: 24px;
            margin-bottom: 16px;
        }

        .badges {
            margin: 20px 0;
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .badge {
            display: inline-flex;
            align-items: center;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            text-decoration: none;
            color: white;
            transition: transform 0.2s, opacity 0.2s;
        }

        .badge:hover {
            transform: translateY(-1px);
            opacity: 0.9;
        }

        .badge-python { 
            background-color: #3776AB; 
        }

        .badge-mit { 
            background-color: #00B0FF; 
        }

        .badge-code { 
            background-color: #000000; 
        }

        code {
            background-color: #f6f8fa;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: 'SF Mono', Monaco, 'Cascadia Code', 'Courier New', monospace;
            font-size: 85%;
        }

        pre {
            background-color: #f6f8fa;
            padding: 16px;
            overflow: auto;
            border-radius: 6px;
            line-height: 1.45;
            margin: 16px 0;
        }

        pre code {
            background-color: transparent;
            padding: 0;
            font-size: 100%;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            margin: 16px 0;
        }

        th, td {
            border: 1px solid #dfe2e5;
            padding: 8px 13px;
            text-align: left;
        }

        th {
            background-color: #f6f8fa;
            font-weight: 600;
        }

        hr {
            border: 0;
            border-top: 1px solid #eaecef;
            margin: 24px 0;
        }

        .footer {
            text-align: center;
            padding: 40px 20px 20px;
            color: #6a737d;
            border-top: 1px solid #eaecef;
            margin-top: 40px;
        }

        ul, ol {
            margin: 16px 0;
            padding-left: 2em;
        }

        li {
            margin: 8px 0;
        }

        a {
            color: #0366d6;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        .container {
            background: white;
            border-radius: 8px;
        }

        @media (max-width: 768px) {
            body {
                padding: 20px 15px;
            }

            table {
                font-size: 14px;
            }

            pre {
                font-size: 12px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔍 Hybrid Search Engine for Technical Documentation</h1>

        <div class="badges">
            <span class="badge badge-python">🐍 Python 3.8+</span>
            <span class="badge badge-mit">📄 MIT License</span>
            <span class="badge badge-code">⚫ Code Style: Black</span>
        </div>

        <p>A production-ready hybrid search and RAG (Retrieval-Augmented Generation) system that combines multiple retrieval strategies for optimal document search and question answering.</p>

        <hr>

        <h2>🎯 Features</h2>

        <table>
            <thead>
                <tr>
                    <th>Component</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Multi-Strategy Retrieval</strong></td>
                    <td>Lexical (TF-IDF, BM25) + Semantic (Embeddings, FAISS)</td>
                </tr>
                <tr>
                    <td><strong>Reciprocal Rank Fusion (RRF)</strong></td>
                    <td>Combines multiple ranking strategies intelligently</td>
                </tr>
                <tr>
                    <td><strong>Cross-Encoder Reranking</strong></td>
                    <td>Improves relevance using transformer-based reranking</td>
                </tr>
                <tr>
                    <td><strong>RAG Pipeline</strong></td>
                    <td>Generates answers using Qwen3 language model</td>
                </tr>
                <tr>
                    <td><strong>Scalable Architecture</strong></td>
                    <td>Modular design for easy extension and experimentation</td>
                </tr>
            </tbody>
        </table>

        <h2>🏗️ Architecture</h2>

        <pre><code>User Query
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
                        └─── Final Answer</code></pre>

        <h2>📦 Installation</h2>

        <h3>1. Clone the Repository</h3>
        <pre><code>git clone https://github.com/MDuarte99/Hybrid-Search-for-Technical-Documentation.git
cd Hybrid-Search-for-Technical-Documentation</code></pre>

        <h3>2. Create Virtual Environment</h3>
        <pre><code># Using venv
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on Linux/Mac
source venv/bin/activate</code></pre>

        <h3>3. Install Dependencies</h3>
        <pre><code>pip install -r requirements.txt</code></pre>

        <h3>4. Set Up Data</h3>
        <p>Place your technical documentation in the appropriate data directory:</p>
        <pre><code>project/data/raw/
└── your_documents.txt</code></pre>

        <h2>🚀 Usage</h2>

        <h3>Run the Complete Pipeline</h3>
        <pre><code>python main.py</code></pre>

        <h3>Interactive Q&A Session</h3>
        <pre><code>from main import run_pipeline
from project.data_loader import load_corpus

# Load your corpus
chunks, metadata, embeddings = load_corpus()

# Ask a question
answer = run_pipeline("How does transformer architecture work?", chunks, embeddings)
print(answer)</code></pre>

        <h2>📊 Retrieval Strategies</h2>

        <h3>1. <strong>TF-IDF Search</strong></h3>
        <ul>
            <li>Traditional term frequency-inverse document frequency</li>
            <li>Excellent for exact keyword matching</li>
            <li>Fast and interpretable</li>
        </ul>

        <h3>2. <strong>BM25 Search</strong></h3>
        <ul>
            <li>Advanced probabilistic retrieval model</li>
            <li>Better term saturation and document length normalization</li>
            <li>Industry standard for lexical search</li>
        </ul>

        <h3>3. <strong>Embedding Search</strong></h3>
        <ul>
            <li>Semantic search using sentence transformers</li>
            <li>Captures contextual meaning</li>
            <li>Handles synonyms and paraphrases</li>
        </ul>

        <h3>4. <strong>FAISS Search</strong></h3>
        <ul>
            <li>Efficient similarity search at scale</li>
            <li>Vector similarity with cosine distance</li>
            <li>Optimized for large document collections</li>
        </ul>

        <h2>🔄 Fusion &amp; Reranking</h2>

        <h3>Reciprocal Rank Fusion (RRF)</h3>
        <ul>
            <li>Combines multiple ranking signals</li>
            <li>Reduces bias from individual retrievers</li>
            <li>Outperforms individual strategies</li>
        </ul>

        <h3>Cross-Encoder Reranking</h3>
        <ul>
            <li>Transformer-based relevance scoring</li>
            <li>Considers query-document pairs jointly</li>
            <li>Significant accuracy improvement</li>
        </ul>

        <h2>💡 RAG Pipeline</h2>
        <p>The system generates contextually aware answers using:</p>
        <ul>
            <li>Retrieved relevant documents as context</li>
            <li>Qwen3 language model for generation</li>
            <li>Grounded responses based on retrieved information</li>
        </ul>

        <h2>📁 Project Structure</h2>
        <pre><code>Hybrid-Search-for-Technical-Documentation/
├── main.py                    # Main pipeline entry point
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation
├── .gitignore                 # Git ignore rules
└── project/
    ├── data_loader.py         # Data ingestion utilities
    ├── retrievers/
    │   ├── tfidf_search.py    # TF-IDF implementation
    │   ├── bm25_search.py     # BM25 implementation
    │   └── embedding_search.py # Semantic search
    ├── vectorstore/
    │   └── faiss_search.py    # FAISS vector store
    ├── fusion/
    │   └── reciprocal_rank_fusion.py # RRF implementation
    ├── reranking/
    │   └── cross_encoder_reranker.py # Reranking logic
    └── generation/
        └── rag_pipeline.py    # Answer generation</code></pre>

        <h2>🧪 Example Queries</h2>
        <pre><code># Technical questions
query = "What are the main components of a transformer model?"

# Comparison questions  
query = "How does BERT differ from GPT?"

# Implementation questions
query = "How do I implement attention mechanism in PyTorch?"</code></pre>

        <h2>📈 Performance Features</h2>
        <ul>
            <li><strong>Parallel Retrieval</strong>: Multiple retrievers run independently</li>
            <li><strong>Efficient Caching</strong>: Embeddings and indices are cached</li>
            <li><strong>Scalable</strong>: FAISS supports million-scale document collections</li>
            <li><strong>Configurable</strong>: Easy to adjust retrieval weights and top-k values</li>
        </ul>

        <h2>🔧 Configuration</h2>
        <p>Key parameters you can adjust in <code>main.py</code>:</p>
        <pre><code># Fusion parameters
fused_results = reciprocal_rank_fusion(results, k=60)  # RRF constant

# Reranking
reranked_results = rerank(query, candidate_docs, top_k=10)

# Retrieval
faiss_results = faiss_search(query, chunks, k=50)</code></pre>

        <h2>🐛 Troubleshooting</h2>
        <table>
            <thead>
                <tr>
                    <th>Issue</th>
                    <th>Solution</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Memory errors</strong></td>
                    <td>Reduce batch sizes in embedding generation</td>
                </tr>
                <tr>
                    <td><strong>Slow FAISS search</strong></td>
                    <td>Decrease k parameter or use GPU</td>
                </tr>
                <tr>
                    <td><strong>Missing dependencies</strong></td>
                    <td>Run <code>pip install -r requirements.txt</code></td>
                </tr>
                <tr>
                    <td><strong>Model download fails</strong></td>
                    <td>Check internet connection or use local cache</td>
                </tr>
            </tbody>
        </table>

        <h2>📝 Requirements</h2>
        <ul>
            <li>Python 3.8+</li>
            <li>8GB+ RAM (16GB recommended)</li>
            <li>GPU optional (for faster embedding generation)</li>
            <li>Disk space: 2GB+ for models and data</li>
        </ul>

        <h2>🤝 Contributing</h2>
        <ol>
            <li>Fork the repository</li>
            <li>Create a feature branch (<code>git checkout -b feature/amazing-feature</code>)</li>
            <li>Commit changes (<code>git commit -m 'Add amazing feature'</code>)</li>
            <li>Push to branch (<code>git push origin feature/amazing-feature</code>)</li>
            <li>Open a Pull Request</li>
        </ol>

        <h2>📄 License</h2>
        <p>This project is licensed under the MIT License - see the <a href="#">LICENSE</a> file for details.</p>

        <h2>🙏 Acknowledgments</h2>
        <ul>
            <li><a href="https://www.sbert.net/">Sentence Transformers</a> for embeddings</li>
            <li><a href="https://github.com/facebookresearch/faiss">FAISS</a> for vector search</li>
            <li><a href="https://github.com/QwenLM/Qwen">Qwen</a> for language model</li>
        </ul>

        <h2>📧 Contact</h2>
        <p><strong>Author</strong>: MDuarte99<br>
        <strong>Project Link</strong>: <a href="https://github.com/MDuarte99/Hybrid-Search-for-Technical-Documentation">https://github.com/MDuarte99/Hybrid-Search-for-Technical-Documentation</a></p>

        <hr>

        <div class="footer">
            <p>⭐ If you find this project useful, please give it a star! ⭐</p>
            <p><strong>Built with 🚀 for Intelligent Document Retrieval</strong></p>
        </div>
    </div>
</body>
</html>

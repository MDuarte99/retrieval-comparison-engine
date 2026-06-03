from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

DATA_DIR = BASE_DIR / "data"

PROCESSED_DIR = DATA_DIR / "processed"

CHUNKS_FILE = (
    PROCESSED_DIR
    / "chunks.json"
)

EMBEDDINGS_FILE = (
    PROCESSED_DIR
    / "embeddings.npy"
)

EMBEDDING_MODEL = (
    "all-MiniLM-L6-v2"
)

RERANK_MODEL = (
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

OLLAMA_MODEL = (
    "qwen2.5:3b"
)

TOP_K_RETRIEVAL = 20

TOP_K_RERANK = 5

TFIDF_WEIGHT = 0.3

BM25_WEIGHT = 0.3

EMBEDDING_WEIGHT = 0.4
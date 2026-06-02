import faiss
import numpy as np

from project.data_loader import (
    load_corpus
)

chunks, metadata, embeddings = (
    load_corpus()
)

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(
    dimension
)

index.add(
    embeddings.astype(
        np.float32
    )
)

faiss.write_index(
    index,
    "project/data/processed/faiss.index"
)
import json
import numpy as np

from project.config.settings import (
    CHUNKS_FILE,
    EMBEDDINGS_FILE
)


def load_corpus():

    with open(
        CHUNKS_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        corpus = json.load(f)

    chunks = corpus["chunks"]

    metadata = corpus["metadata"]

    embeddings = np.load(
        EMBEDDINGS_FILE
    )

    return (
        chunks,
        metadata,
        embeddings
    )
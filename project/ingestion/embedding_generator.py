import numpy as np

from sentence_transformers import (
    SentenceTransformer
)


MODEL_NAME = (
    "all-MiniLM-L6-v2"
)

model = SentenceTransformer(
    MODEL_NAME
)


def generate_embeddings(chunks):

    print(
        f"Generating embeddings for {len(chunks)} chunks..."
    )

    embeddings = model.encode(
        chunks,
        show_progress_bar=True,
        convert_to_numpy=True
    )

    return embeddings


def save_embeddings(
    embeddings,
    output_file
):

    np.save(
        output_file,
        embeddings
    )

    print(
        f"Embeddings saved to {output_file}"
    )


def load_embeddings(
    input_file
):

    return np.load(
        input_file
    )
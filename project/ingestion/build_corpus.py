import json

from pathlib import Path

from github_loader import (
    clone_all
)

from markdown_parser import (
    extract_documents
)

from chunker import (
    chunk_text
)

from embedding_generator import (
    generate_embeddings,
    save_embeddings
)


BASE_DIR = (
    Path(__file__).parent.parent
)

RAW_DIR = (
    BASE_DIR
    / "data"
    / "raw"
)

PROCESSED_DIR = (
    BASE_DIR
    / "data"
    / "processed"
)

CHUNKS_FILE = (
    PROCESSED_DIR
    / "chunks.json"
)

EMBEDDINGS_FILE = (
    PROCESSED_DIR
    / "embeddings.npy"
)


def build_corpus():

    PROCESSED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    print(
        "\nStep 1: Cloning repositories..."
    )

    clone_all()

    print(
        "\nStep 2: Reading documentation..."
    )

    all_documents = []

    for repository in RAW_DIR.iterdir():

        if repository.is_dir():

            docs = extract_documents(
                repository
            )

            all_documents.extend(
                docs
            )

    print(
        f"Loaded {len(all_documents)} documents"
    )

    print(
        "\nStep 3: Chunking..."
    )

    chunks = []

    metadata = []

    for document in all_documents:

        doc_chunks = chunk_text(
            document["content"],
            chunk_size=500,
            overlap=50
        )

        for chunk in doc_chunks:

            chunks.append(chunk)

            metadata.append(
                {
                    "source":
                    document["source"]
                }
            )

    print(
        f"Generated {len(chunks)} chunks"
    )

    print(
        "\nStep 4: Generating embeddings..."
    )

    embeddings = generate_embeddings(
        chunks
    )

    print(
        "\nStep 5: Saving corpus..."
    )

    with open(
        CHUNKS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "chunks": chunks,
                "metadata": metadata
            },
            f,
            ensure_ascii=False,
            indent=2
        )

    save_embeddings(
        embeddings,
        EMBEDDINGS_FILE
    )

    print(
        "\nCorpus successfully built."
    )


if __name__ == "__main__":

    build_corpus()
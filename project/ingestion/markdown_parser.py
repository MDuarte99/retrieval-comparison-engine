from pathlib import Path


SUPPORTED_EXTENSIONS = [
    ".md",
    ".mdx",
    ".rst"
]


def extract_documents(root_path):

    root_path = Path(root_path)

    documents = []

    for file in root_path.rglob("*"):

        if file.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue

        try:

            text = file.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            if len(text.strip()) > 100:

                documents.append(
                    {
                        "source": str(file),
                        "content": text
                    }
                )

        except Exception as e:

            print(
                f"Error reading {file}: {e}"
            )

    return documents
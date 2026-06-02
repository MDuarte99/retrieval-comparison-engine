from pathlib import Path
import subprocess


REPOSITORIES = {
    "langchain": "https://github.com/langchain-ai/langchain.git",
    "llama_index": "https://github.com/run-llama/llama_index.git",
    "chroma": "https://github.com/chroma-core/chroma.git",
    "mlflow": "https://github.com/mlflow/mlflow.git",
    "ollama": "https://github.com/ollama/ollama.git",
}


RAW_DATA_DIR = (
    Path(__file__).parent.parent
    / "data"
    / "raw"
)


def clone_repository(name, repo_url):

    destination = RAW_DATA_DIR / name

    if destination.exists():

        print(
            f"[SKIP] {name} already exists."
        )

        return

    print(
        f"[CLONE] {name}"
    )

    subprocess.run(
        [
            "git",
            "clone",
            "--depth",
            "1",
            repo_url,
            str(destination)
        ],
        check=True
    )


def clone_all():

    RAW_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    for name, repo_url in REPOSITORIES.items():

        clone_repository(
            name,
            repo_url
        )


if __name__ == "__main__":

    clone_all()
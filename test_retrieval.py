from project.data_loader import load_corpus

chunks, metadata, embeddings = load_corpus()

print(f"Chunks loaded: {len(chunks)}")

print("\nFirst chunk:\n")
print(chunks[0][:500])
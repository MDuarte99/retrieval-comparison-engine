# Hybrid Search for Technical Documentation

A lightweight AI Retrieval System that compares lexical search (TF-IDF), semantic search (Sentence Transformers), and hybrid retrieval approaches.

## Motivation

Modern AI systems rarely rely on a single retrieval strategy.

Traditional lexical search works well for exact keyword matches, while semantic search captures contextual meaning through embeddings.

This project demonstrates how combining both approaches improves document retrieval quality for technical documentation.

## Features

* TF-IDF Retrieval
* Semantic Retrieval using Sentence Transformers
* Hybrid Search (Lexical + Semantic)
* Document Ranking
* Similarity Scoring
* Modular Retrieval Architecture

## Tech Stack

* Python
* Scikit-Learn
* Sentence Transformers
* NumPy

## Example Query

Query:

"How can I deploy a machine learning model?"

Top Hybrid Result:

"FastAPI can be used to deploy machine learning models as REST APIs."

## Future Improvements

* BM25 Retrieval
* Cross-Encoder Reranking
* Vector Database Integration (ChromaDB)
* Retrieval Evaluation Metrics
* RAG Pipeline Integration

## Why This Project Matters

Hybrid retrieval is a common architecture behind production AI systems, including:

* RAG Applications
* AI Assistants
* Enterprise Search Systems
* Documentation Agents
* Knowledge Bases

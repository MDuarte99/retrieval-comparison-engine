from tfidf_search import TFIDFSearch
from embedding_search import EmbeddingSearch


class HybridSearch:

    def __init__(self, documents):

        self.documents = documents

        self.tfidf_engine = TFIDFSearch(
            documents
        )

        self.embedding_engine = EmbeddingSearch(
            documents
        )

    def search(self, query, top_k=5):

        tfidf_results = self.tfidf_engine.search(
            query,
            top_k=len(self.documents)
        )

        embedding_results = self.embedding_engine.search(
            query,
            top_k=len(self.documents)
        )

        scores = {}

        for result in tfidf_results:

            scores[result["document"]] = {

                "tfidf": result["score"],

                "embedding": 0
            }

        for result in embedding_results:

            doc = result["document"]

            if doc not in scores:

                scores[doc] = {

                    "tfidf": 0,

                    "embedding": 0
                }

            scores[doc]["embedding"] = result["score"]

        ranked_results = []

        for doc, values in scores.items():

            final_score = (

                0.5 * values["tfidf"]

                +

                0.5 * values["embedding"]

            )

            ranked_results.append(
                {
                    "document": doc,
                    "score": final_score,
                    "tfidf": values["tfidf"],
                    "embedding": values["embedding"]
                }
            )

        ranked_results.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranked_results[:top_k]
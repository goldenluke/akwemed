import json
from sentence_transformers import SentenceTransformer, util


class ClinicalRAG:

    def __init__(self, path):

        with open(path, "r") as f:
            self.protocols = json.load(f)

        self.model = SentenceTransformer(
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )

        texts = [p["texto"] for p in self.protocols]

        self.embeddings = self.model.encode(
            texts,
            convert_to_tensor=True
        )

    def query(self, text):

        q = self.model.encode(text, convert_to_tensor=True)

        scores = util.cos_sim(q, self.embeddings)[0]

        best = scores.argmax().item()

        return self.protocols[best]

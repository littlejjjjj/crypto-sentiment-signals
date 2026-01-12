from transformers import pipeline

class SentimentModel:
    def __init__(self):
        self.model = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def score(self, text: str) -> float:
        if not text or not text.strip():
            return 0.0
        
        result = self.model(text[:512])[0]
        label = result["label"]
        score = result["score"]

        return score if label == "POSITIVE" else -score

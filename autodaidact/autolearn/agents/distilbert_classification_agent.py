# autodaidact/autolearn/agents/distilbert_classification_agent.py
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch

class DistilBERTClassificationAgent:
    def __init__(self, model_name='distilbert-base-uncased'):
        self.tokenizer = DistilBertTokenizer.from_pretrained(model_name)
        self.model = DistilBertForSequenceClassification.from_pretrained(model_name)

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
        prediction = outputs.logits.argmax(-1).item()
        return prediction

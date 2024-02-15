from autodaidact.autolearn.models.huggingface_wrapper import HuggingFaceWrapper
from transformers import DistilBertForSequenceClassification

class DistilBERTClassificationAgent:
    def __init__(self, model_name='distilbert-base-uncased'):
        self.model_wrapper = HuggingFaceWrapper(model_name=model_name, model_class=DistilBertForSequenceClassification)

    def classify_text(self, text):
        encoded_input = self.model_wrapper.encode([text])
        prediction = self.model_wrapper.predict(encoded_input)
        # Additional logic to convert prediction to label
        return prediction

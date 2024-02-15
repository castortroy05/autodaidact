from transformers import AutoModel, AutoTokenizer
import torch

class HuggingFaceWrapper:
    def __init__(self, model_name):
        """
        Initializes the model and tokenizer based on the specified model name.
        
        Parameters:
            model_name (str): The name of the model to load. This can be any model from
                              Hugging Face's model hub.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def encode(self, texts, max_length=512, padding=True, truncation=True, return_tensors="pt"):
        """
        Encodes a list of texts into model-ready input formats.
        
        Parameters:
            texts (list[str]): The list of texts to encode.
            max_length (int): Maximum length of the tokenized input.
            padding (bool): Whether to pad the input to max_length.
            truncation (bool): Whether to truncate the input to max_length.
            return_tensors (str): The type of tensors to return. Usually "pt" for PyTorch.
            
        Returns:
            A dictionary containing the encoded inputs suitable for the model.
        """
        return self.tokenizer(texts, max_length=max_length, padding=padding, truncation=truncation, return_tensors=return_tensors)

    def predict(self, encoded_inputs):
        """
        Predicts the output based on the encoded inputs using the loaded model.
        
        Parameters:
            encoded_inputs (dict): The output from the `encode` method, containing
                                   tokenized inputs for the model.
        
        Returns:
            The model's predictions.
        """
        with torch.no_grad():
            outputs = self.model(**encoded_inputs)
        return outputs

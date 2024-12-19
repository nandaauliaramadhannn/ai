import torch
from transformers import BertTokenizer, BertForSequenceClassification

print("CUDA available:", torch.cuda.is_available())

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForSequenceClassification.from_pretrained("bert-base-uncased")
print("Hugging face model loaded successfully")
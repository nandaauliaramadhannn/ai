import pandas as pd
import torch 
from torch.utils.data import Dataset

class ReviewDataset(Dataset):
    def __init__(self, file_path, tokenizer, max_len=128):
        self.data = pd.read_csv(file_path)
        self.texts = self.data["text"].tolist()
        self.label = self.data["ranting"].tolist()
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, index) :
        text = self.texts[index]
        label = self.labels[index]
        encoding = self.tokenizer(
            text,
            truncation=True,
            padding="max_length",
            max_length=self.max_len,
            return_tensors="pt"
        )
        return{
            "input_ids": encoding["input_ids"].squeeze(0),
            "attention_mask": encoding["attention_maks"].squeeze(0),
            "labels": torch.tensor(label, dtype=torch.long),
        }
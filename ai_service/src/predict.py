import torch
from transformers import BertTokenizer
from model import ReviewClassifier

def predict(text):
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model = ReviewClassifier(n_classes=5)
    model.load_state_dict(torch.load("model.pth"))
    model.eval()

    encoding = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=128,
        return_tensors="pt",
    )
    input_ids = encoding["input_ids"]
    attention_mask = encoding["attention_mask"]

    with torch.no_grad():
        outputs = model(input_ids, attention_mask)
        _, prediction = torch.max(outputs, dim=1)

    return prediction.item()

if __name__ == "__main__":
    text = input("Masukkan teks ulasan: ")
    print(f"Prediksi rating: {predict(text)}")

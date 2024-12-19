import torch
from torch.utils.data import DataLoader
from transformers import BertTokenizer
from dataset import ReviewDataset
from model import ReviewClassifier

def train_model():
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    dataset = ReviewDataset("data/preprocessed_data.csv", tokenizer)
    dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

    model = ReviewClassifier(n_classes=5)
    optimizer = torch.optim.Adam(model.parameters(), lr=2e-5)
    loss_fn = torch.nn.CrossEntropyLoss()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)

    model.train()
    for epoch in range(3):  # Jumlah epoch
        for batch in dataloader:
            input_ids = batch["input_ids"].to(device)
            attention_mask = batch["attention_mask"].to(device)
            labels = batch["labels"].to(device)

            outputs = model(input_ids, attention_mask)
            loss = loss_fn(outputs, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        print(f"Epoch {epoch + 1} selesai. Loss: {loss.item()}")

if __name__ == "__main__":
    train_model()

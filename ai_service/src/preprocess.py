import pandas as pd
import re 

def clean_text(text):
    """ Membersihkan teks ."""
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # Hapus URL
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)  # Hapus karakter khusus
    text = re.sub(r"\s+", " ", text).strip()  # Hapus spasi berlebih
    return text

def preprocess(input_file, output_file):
    """ proses data mentah dan simpan sebagi file csv."""
    df = pd.read_csv(input_file)
    df['text'] = df['text'].apply(clean_text)
    df = df[df["text"].str.len() > 0]  # Hapus baris kosong
    df = df[["text", "ranting"]] # ambil kolom yang di perlukan
    df.to_csv(output_file, index=False)
    print(f"data preprocessed dan disimpan di '{output_file}'.")

if __name__ == "__main__":
    preprocess_data("data/scraped-data.csv", "data/preprocessed-data.csv")
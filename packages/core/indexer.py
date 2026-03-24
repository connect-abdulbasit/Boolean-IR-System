import os
import re
import json
from .preprocessing import preprocess_text, load_stopwords, apply_stemming

def build_indexes(data_path, stopwords_path):
    stopwords = load_stopwords(stopwords_path)
    inverted_index = {}
    positional_index = {}
    files = sorted(
        [f for f in os.listdir(data_path) if os.path.isfile(os.path.join(data_path, f))],
        key=lambda f: int(re.search(r'(\d+)', f).group(1))
    )
    for filename in files:
        filepath = os.path.join(data_path, filename)
        doc_id = int(re.search(r'(\d+)', filename).group(1))
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
        tokens = preprocess_text(text, set())
        for position, word in enumerate(tokens):
            if word in stopwords:
                continue
            word = apply_stemming(word)
            if word not in inverted_index:
                inverted_index[word] = []
            if doc_id not in inverted_index[word]:
                inverted_index[word].append(doc_id)
            if word not in positional_index:
                positional_index[word] = {}
            if doc_id not in positional_index[word]:
                positional_index[word][doc_id] = []
            positional_index[word][doc_id].append(position)
    return inverted_index, positional_index

def save_indexes(inverted_index, positional_index, index_dir="indexes"):
    os.makedirs(index_dir, exist_ok=True)
    with open(os.path.join(index_dir, "inverted_index.json"), "w") as f:
        json.dump(inverted_index, f)
    with open(os.path.join(index_dir, "positional_index.json"), "w") as f:
        json.dump(positional_index, f)
    print(f"Indexes saved successfully in {index_dir}!")

def load_indexes(index_dir="indexes"):
    with open(os.path.join(index_dir, "inverted_index.json"), "r") as f:
        inverted = json.load(f)
    with open(os.path.join(index_dir, "positional_index.json"), "r") as f:
        positional = json.load(f)
    positional = {
        term: {int(doc): positions for doc, positions in docs.items()}
        for term, docs in positional.items()
    }
    return inverted, positional

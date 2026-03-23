import os
import json
from preprocessing import preprocess_text, load_stopwords

def build_indexes(data_path, stopwords_path):
    stopwords = load_stopwords(stopwords_path)
    inverted_index = {}
    positional_index = {}
    doc_id = 0
    for filename in os.listdir(data_path):
        filepath = os.path.join(data_path, filename)
        if os.path.isfile(filepath):
            doc_id += 1
            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()
            tokens = preprocess_text(text, stopwords)
            for position, word in enumerate(tokens):
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

def save_indexes(inverted_index, positional_index):
    os.makedirs("indexes", exist_ok=True)
    with open("indexes/inverted_index.json", "w") as f:
        json.dump(inverted_index, f)
    with open("indexes/positional_index.json", "w") as f:
        json.dump(positional_index, f)
    print("Indexes saved successfully!")

def load_indexes():
    with open("indexes/inverted_index.json", "r") as f:
        inverted = json.load(f)
    with open("indexes/positional_index.json", "r") as f:
        positional = json.load(f)
    positional = {
        term: {int(doc): positions for doc, positions in docs.items()}
        for term, docs in positional.items()
    }
    return inverted, positional
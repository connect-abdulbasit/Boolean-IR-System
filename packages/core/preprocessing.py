import re
from nltk.stem import PorterStemmer

def load_stopwords(filepath):
    stopwords = set()
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                word = line.strip().lower()
                if word:
                    stopwords.add(word)
    except FileNotFoundError:
        print("Stopwords file not found!")
    return stopwords

def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = text.lower()
    return text

def tokenize(text):
    return text.split()

def remove_stopwords(tokens, stopwords):
    return [word for word in tokens if word not in stopwords]

def preprocess_text(text, stopwords):
    text = clean_text(text)
    tokens = tokenize(text)
    tokens = remove_stopwords(tokens, stopwords)
    return tokens

stemmer = PorterStemmer()

def apply_stemming(word):
    return stemmer.stem(word)

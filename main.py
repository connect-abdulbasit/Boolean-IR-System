from indexer import build_indexes, save_indexes, load_indexes
from queryprocessor import process_query
import os

DATA_PATH = "data/documents"
STOPWORDS_PATH = "data/stopwords/stopwords-list.txt"


def main():
    inverted, positional = build_indexes(DATA_PATH, STOPWORDS_PATH)
    save_indexes(inverted, positional)
    while True:
        query = input("Enter your query: ") 
        total_docs = len([f for f in os.listdir(DATA_PATH) if os.path.isfile(os.path.join(DATA_PATH, f))])
        results = process_query(query, inverted, positional, total_docs)
        print("Results:", results)

if __name__ == "__main__":
    main()
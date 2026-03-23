from indexer import build_indexes, save_indexes, load_indexes

DATA_PATH = "data/documents"
STOPWORDS_PATH = "data/stopwords/stopwords-list.txt"


def main():
    inverted, positional = build_indexes(DATA_PATH, STOPWORDS_PATH)
    save_indexes(inverted, positional)

if __name__ == "__main__":
    main()
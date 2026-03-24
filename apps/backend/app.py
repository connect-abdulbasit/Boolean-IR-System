import os
import sys
import shutil
from flask import Flask, request, jsonify
from flask_cors import CORS

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from packages.core.indexer import build_indexes, save_indexes, load_indexes
from packages.core.query_processor import process_query

app = Flask(__name__)

CORS(app, resources={r"/*": {
    "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
    "methods": ["GET", "POST", "OPTIONS"],
    "allow_headers": ["Content-Type", "Authorization"]
}})

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
DATA_PATH = os.path.join(BASE_DIR, "data/documents")
STOPWORDS_PATH = os.path.join(BASE_DIR, "data/stopwords/stopwords-list.txt")
INDEX_PATH = os.path.join(BASE_DIR, "indexes")


@app.route("/health", methods=["GET"])
def health():
    print("Checking server health status...")
    return jsonify({"status": "ok"}), 200


@app.route("/build", methods=["POST"])
def build():
    try:
        print("Starting the index building process...")
        inverted, positional = build_indexes(DATA_PATH, STOPWORDS_PATH)
        print(f"Index build complete. Processed {len(inverted)} unique terms.")
        save_indexes(inverted, positional, INDEX_PATH)
        print(f"Saved the newly built indexes to: {INDEX_PATH}")
        return jsonify({"message": "Indexes built successfully!"})
    except Exception as e:
        print(f"An error occurred during the build: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/search", methods=["POST"])
def search():
    try:
        print("Processing a new search request...")
        data = request.json
        query = data.get("query", "")
        print(f"Searching for: '{query}'")

        inverted, positional = load_indexes(INDEX_PATH)
        print(f"Loaded existing index data ({len(inverted)} terms).")

        total_docs = len(set(doc for docs in inverted.values() for doc in docs))
        print(f"Scanning through {total_docs} documents...")

        result = process_query(query, inverted, positional, total_docs)
        print(f"Search finished. Found {len(result)} matching results.")

        return jsonify({"documents": sorted(result)})
    except Exception as e:
        print(f"Search failed due to an error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@app.route("/document/<int:doc_id>", methods=["GET"])
def get_document(doc_id):
    try:
        print(f"Fetching content for document {doc_id}...")
        filename = f"speech_{doc_id}.txt"
        filepath = os.path.join(DATA_PATH, filename)

        if not os.path.exists(filepath):
            print(f"Document {filename} not found at {filepath}")
            return jsonify({"error": "Document not found"}), 404

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        return jsonify({
            "id": doc_id,
            "filename": filename,
            "content": content
        })
    except Exception as e:
        print(f"Failed to fetch document {doc_id}: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Initializing system... cleaning up old index files.")
    if os.path.exists(INDEX_PATH):
        shutil.rmtree(INDEX_PATH)

    print("Rebuilding search indexes for a fresh start.")
    try:
        inverted, positional = build_indexes(DATA_PATH, STOPWORDS_PATH)
        save_indexes(inverted, positional, INDEX_PATH)
        print("System is ready. Indexes have been rebuilt.")
    except Exception as e:
        print(f"Could not rebuild indexes during startup: {e}")

    print("Starting backend server on port 5000...")
    app.run(debug=True, port=5000)
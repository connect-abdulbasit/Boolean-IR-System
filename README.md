# 🔍 Boolean Information Retrieval System

A professional, web-based Boolean Information Retrieval (IR) system built with **Python (Flask)** and **React**. This system enables efficient searching through document collections using Boolean logic, proximity operators, and advanced text preprocessing.

---

## ✨ Features

-   **Boolean Logic Retrieval**: Full support for `AND`, `OR`, and `NOT` operators with standard precedence.
-   **Proximity Search**: Find terms within a specific distance using the `NEAR/k` operator (e.g., `war peace /3`).
-   **Advanced Text Preprocessing**:
    -   **Porter Stemming**: Normalizes words (e.g., "running" → "run") for better recall.
    -   **Stop Word Removal**: Filters out common English words to improve search relevance.
-   **Automated Indexing**:
    -   Builds **Inverted Index** and **Positional Index** automatically on backend startup.
    -   Incremental indexing via specialized `build` endpoint.
-   **Modern User Interface**:
    -   Responsive React application with **Tailwind CSS**.
    -   Clean results display with document snippets.
    -   Integrated **Document Viewer** for reading full texts.

---

## 🛠 Tech Stack

-   **Backend**: Python 3.10+, Flask, Porter Stemmer
-   **Frontend**: React 18+, Vite, Tailwind CSS
-   **Core Logic**: Modular Python packages for indexing and query processing.

---

## 🚀 Getting Started

### Prerequisites

-   **Python 3.10+**
-   **Node.js 18+** & **npm**

### 1. Backend Setup

1.  Navigate to the backend directory:
    ```bash
    cd apps/backend
    ```

2.  Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\\Scripts\\activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Run the Flask server:
    ```bash
    python app.py
    ```
    The server will start on `http://localhost:5000`. It will automatically rebuild the indexes on the first run.

### 2. Frontend Setup

1.  Navigate to the frontend directory:
    ```bash
    cd apps/frontend
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

3.  Run the development server:
    ```bash
    npm run dev
    ```
    The application will be available at `http://localhost:3000`.

---

## 📖 Usage Guide

1.  **Boolean Queries**: 
    -   `running AND basit` (Finds documents containing both terms)
    -   `fast OR slow` (Finds documents containing either term)
    -   `apple NOT fruit` (Finds documents containing "apple" but not "fruit")
    -   `(king OR queen) AND castle` (Supports parentheses for grouping)

2.  **Proximity Queries**:
    -   `war peace /3` (Finds documents where "war" and "peace" are within 3 words of each other)

3.  **Viewing Results**:
    -   Click on any search result to view the full document text in the detail page.

---

## 📂 Project Structure

```text
Boolean-IR-System/
├── apps/
│   ├── backend/           # Flask API
│   │   ├── app.py         # Main entry point & API endpoints
│   │   └── requirements.txt
│   └── frontend/          # React + Vite application
│       ├── src/           # React components, pages, services
│       └── vite.config.js
├── packages/
│   └── core/              # Shared logic for IR
│       ├── indexer.py      # Inverted & Positional index logic
│       ├── preprocessing.py# Stemming & Stopword removal
│       └── query_processor.py # Boolean & Proximity query engine
├── data/
│   ├── documents/         # Raw text files (Speeches)
│   └── stopwords/         # Stopwords list
├── indexes/               # Generated index data (JSON)
└── README.md
```

---

## 🔌 API Documentation

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/health` | `GET` | Check server health status |
| `/search` | `POST` | Execute a Boolean/Proximity search |
| `/document/<id>` | `GET` | Retrieve full content of a document |
| `/build` | `POST` | Manually trigger an index rebuild |

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
# doc_qa_bot
# Document Question Answering Bot using RAG

## Project Description

This project is a Retrieval-Augmented Generation (RAG) based Question Answering Bot that answers user queries using only the information contained in a collection of PDF documents. The system retrieves relevant document chunks from a vector database, provides them as context to a Large Language Model (LLM), and generates accurate answers along with source citations.

If the answer is not present in the uploaded documents, the bot responds:

> I don't know based on the provided documents.

---

## Features

* PDF document ingestion
* Automatic document chunking
* Semantic embeddings generation
* ChromaDB vector storage
* Similarity-based retrieval
* Threshold-based filtering
* LLM-powered answer generation
* Source citation support
* Hallucination reduction using RAG
* Interactive command-line chatbot

---

## Tech Stack

| Component                | Library / Tool                | Version |
| ------------------------ | ----------------------------- | ------- |
| Language                 | Python                        | 3.10+   |
| PDF Loading              | pypdf                         | 5.x     |
| Document Loader          | langchain-community           | 0.3.x   |
| Text Splitting           | langchain-text-splitters      | 0.3.x   |
| Embeddings               | sentence-transformers         | 4.x     |
| Embedding Wrapper        | langchain-huggingface         | 0.1.x   |
| Embedding Model          | all-MiniLM-L6-v2              | Latest  |
| Vector Database          | ChromaDB                      | 1.x     |
| Vector Store Integration | langchain-chroma              | 0.2.x   |
| LLM Framework            | LangChain                     | 0.3.x   |
| Local LLM                | Ollama                        | Latest  |
| LLM Models               | Llama 3 / Qwen3 / DeepSeek-R1 | Latest  |
| Version Control          | Git                           | Latest  |

---

## Architecture Overview

### Ingestion Pipeline

```text
PDF Documents
      │
      ▼
Document Loader
(PyPDFLoader)
      │
      ▼
Chunking
(RecursiveCharacterTextSplitter)
      │
      ▼
Embedding Model
(all-MiniLM-L6-v2)
      │
      ▼
Vector Database
(ChromaDB)
```

### Question Answering Pipeline

```text
User Query
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Apply Similarity Threshold
      │
      ▼
Build Context
      │
      ▼
LLM (Ollama)
      │
      ▼
Answer + Source Citation
```

### Complete RAG Workflow

```text
PDFs
 ↓
Load Documents
 ↓
Chunk Documents
 ↓
Generate Embeddings
 ↓
Store in ChromaDB
 ↓
User Query
 ↓
Similarity Search
 ↓
Threshold Filtering
 ↓
Context Generation
 ↓
LLM Response
 ↓
Answer with Citation
```

---

## Chunking Strategy

### Strategy Used

Recursive Character Text Splitter

```python
RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

### Why This Strategy?

* Preserves sentence and paragraph structure.
* Prevents important information from being split incorrectly.
* Maintains contextual continuity using chunk overlap.
* Suitable for educational and technical PDF documents.

### Configuration

```text
Chunk Size: 500 characters
Chunk Overlap: 50 characters
```

---

## Embedding Model

### Model Used

```text
sentence-transformers/all-MiniLM-L6-v2
```

### Why This Model?

* Lightweight and efficient.
* Produces high-quality semantic embeddings.
* Excellent performance for similarity search.
* Runs locally without API costs.
* Widely adopted in RAG applications.

---

## Vector Database

### Database Used

```text
ChromaDB
```

### Why ChromaDB?

* Open source.
* Easy integration with LangChain.
* Persistent local storage.
* Fast similarity search.
* Ideal for small to medium-sized document collections.

---

## Project Structure

```text
example_rag/
│
├── datas/
│   ├── AI_agent.pdf
│   ├── Artificial_intelligence.pdf
│   ├── Cloud_computing.pdf
│   └── Computer_network.pdf
│
├── vector_db/
│
├── ingest.py
├── retriever.py
├── llm_service.py
├── qa.py
│
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd example_rag
```

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama:

https://ollama.com

Pull a model:

```bash
ollama pull llama3
```

### 5. Add PDF Documents

Place all PDF files inside the `datas/` directory.

Example:

```text
datas/
├── AI_agent.pdf
├── Artificial_intelligence.pdf
├── Cloud_computing.pdf
└── Computer_network.pdf
```

### 6. Build the Vector Database

```bash
python ingest.py
```

Expected Output:

```text
Loaded X documents
Created Y chunks
Vector database created successfully
```

### 7. Run the Chatbot

```bash
python qa.py
```

---

## Environment Variables

### Optional Hugging Face Token

Create a `.env` file:

```env
HF_TOKEN=your_huggingface_token
```

### Windows

```powershell
$env:HF_TOKEN="your_token_here"
```

### Linux/macOS

```bash
export HF_TOKEN="your_token_here"
```

### Security Note

Never commit:

```text
.env
HF_TOKEN
API Keys
```

Add the following to `.gitignore`:

```text
.env
vector_db/
__pycache__/
venv/
```

---

## Example Queries

### Knowledge Base Queries

1. What is an AI agent?
2. What are the orchestration patterns used in AI agents?
3. What is Artificial Intelligence?
4. What is machine learning?
5. What is deep learning?
6. What are the characteristics of cloud computing?
7. What is a computer network?

### Expected Answer Themes

| Query                       | Expected Theme                              |
| --------------------------- | ------------------------------------------- |
| What is an AI agent?        | Definition and characteristics of AI agents |
| What is machine learning?   | Learning from data and prediction           |
| What is deep learning?      | Neural networks and AI                      |
| What is cloud computing?    | Cloud services and characteristics          |
| What is a computer network? | Communication between connected devices     |

---

## Negative Test Cases

These questions are intentionally outside the document knowledge base:

1. Tell me about Mars.
2. What is Blockchain?
3. What is Quantum Computing?
4. Who won the FIFA World Cup 2022?

Expected Response:

```text
I don't know based on the provided documents.
```

---

## Source Citation Support

Each answer includes source references extracted from document metadata.

Example:

```text
Answer:
Deep learning is a subset of machine learning that uses artificial neural networks.

Source:
Artificial_intelligence.pdf (Page 8)
```

---

## Known Limitations

### 1. Limited to Uploaded Documents

The bot can only answer questions whose information exists in the provided PDFs.

### 2. Retrieval Sensitivity

Performance depends on:

* Chunk size
* Chunk overlap
* Embedding quality
* Similarity threshold

Improper configuration may retrieve irrelevant chunks.

### 3. Hallucination Risk

Although RAG reduces hallucinations, the LLM may occasionally generate unsupported information if prompts are not sufficiently restrictive.

### 4. No Multi-Document Reasoning

The system retrieves relevant chunks but does not perform advanced reasoning across multiple documents.

### 5. Context Window Constraints

Large contexts may exceed the LLM's maximum token limit.

### 6. PDF Quality Dependency

Scanned PDFs or image-only PDFs may reduce extraction accuracy because text extraction relies on machine-readable content.

### 7. No Conversational Memory

Each query is processed independently. Previous conversations are not retained.

---

## Future Improvements

* Web-based interface using Streamlit or FastAPI
* Conversational memory support
* Hybrid search (keyword + semantic retrieval)
* Reranking models for improved retrieval accuracy
* Multi-document reasoning
* OCR support for scanned PDFs
* Citation highlighting within answers

---

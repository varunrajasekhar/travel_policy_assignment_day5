from __future__ import annotations

import json
from pathlib import Path

from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


KNOWLEDGE_DIR = Path(__file__).resolve().parent / "knowledge"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

_vector_store: InMemoryVectorStore | None = None
_chunk_count = 0


def load_knowledge_documents() -> list[Document]:
    """Load the company's travel-policy Markdown files as LangChain Documents.

    TODO 1
    Complete this function so it:
    - reads every .md file from KNOWLEDGE_DIR
    - processes files in deterministic filename order
    - creates one Document per file
    - stores the filename in metadata["source"]
    - stores the filename without .md in metadata["topic"]
    - returns the list of Documents
    """
    # TODO: implement
    raise NotImplementedError("TODO 1: load the knowledge documents")


def initialize_rag() -> InMemoryVectorStore:
    """Build and cache the semantic travel-policy knowledge base.

    TODO 2
    Use the same Day 2 RAG architecture demonstrated in class:
    1. Load the policy Documents.
    2. Split them with RecursiveCharacterTextSplitter.
    3. Create HuggingFace MiniLM embeddings on CPU.
    4. Add the chunks to an InMemoryVectorStore.
    5. Cache the vector store so it is built only once per Python process.
    6. Update _chunk_count with the number of chunks.

    Required splitter configuration:
        chunk_size=550
        chunk_overlap=80

    Required embedding configuration:
        model_name=EMBEDDING_MODEL_NAME
        model_kwargs={"device": "cpu"}
        encode_kwargs={"normalize_embeddings": True}
    """
    global _vector_store, _chunk_count

    # TODO: implement
    raise NotImplementedError("TODO 2: initialize the RAG pipeline")


def search_travel_knowledge(query: str, k: int = 4) -> str:
    """Semantically search the travel-policy knowledge base.

    IMPORTANT: Keep this as a normal Python function. Do not add @tool.

    TODO 3
    Complete this function so it:
    - gets the cached vector store from initialize_rag()
    - clamps k to the inclusive range 1..6
    - calls similarity_search(query, k=safe_k)
    - preserves retrieval order
    - returns JSON text containing search_type, embedding_model, and results
    - includes rank, source, topic, and content for every retrieved chunk
    - never invents policy text or source names
    """
    # TODO: implement
    raise NotImplementedError("TODO 3: implement semantic retrieval")

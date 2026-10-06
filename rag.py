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
    """Load the company's travel-policy Markdown files as LangChain Documents."""
    documents: list[Document] = []
    for file_path in sorted(KNOWLEDGE_DIR.glob("*.md")):
        content = file_path.read_text(encoding="utf-8")
        metadata = {
            "source": file_path.name,
            "topic": file_path.stem,
        }
        documents.append(Document(page_content=content, metadata=metadata))
    return documents


def initialize_rag() -> InMemoryVectorStore:
    """Build and cache the semantic travel-policy knowledge base."""
    global _vector_store, _chunk_count

    if _vector_store is not None:
        return _vector_store

    print("Loading travel-policy knowledge documents")
    splitter = RecursiveCharacterTextSplitter(chunk_size=550, chunk_overlap=80)
    chunks = splitter.split_documents(load_knowledge_documents())

    _chunk_count = len(chunks)
    print(f"Created {_chunk_count} knowledge chunks")
    print("Loading the embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )
    _vector_store = InMemoryVectorStore(embedding=embeddings)
    _vector_store.add_documents(chunks)
    return _vector_store


def search_travel_knowledge(query: str, k: int = 4) -> str:
    """Semantically search the travel-policy knowledge base."""
    vector_store = initialize_rag()
    safe_k = max(1, min(k, 6))
    results = vector_store.similarity_search(query, k=safe_k)

    search_results = {
        "search_type": "semantic",
        "embedding_model": EMBEDDING_MODEL_NAME,
        "results": [],
    }

    for rank, chunk in enumerate(results, start=1):
        search_results["results"].append(
            {
                "rank": rank,
                "source": chunk.metadata["source"],
                "topic": chunk.metadata["topic"],
                "content": chunk.page_content,
            }
        )

    return json.dumps(search_results)

from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import os
import shutil

def load_documents(doc_path = "datas"):
    loader = DirectoryLoader(
        path=doc_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()
    print(f"Loaded {len(documents)} documents")
    return documents

def chunk_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        )
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")
    return chunks

def get_embedding():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

def store_in_vectordb(chunks, embeddings):

    if os.path.exists("vector_db"):
        shutil.rmtree("vector_db")

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vector_db"
    )

    print("Vector database created successfully")
    print(f"Number of documents in vector database: {vectordb._collection.count()} ")
    return vectordb

def main():
    print("Main function")

    #Load all pdf files in the directory
    documents = load_documents()

    #Chunking the pdf files
    chunks = chunk_documents(documents)
    for i, chunk in enumerate(chunks[:3]):
        print(f"\nChunk {i+1}")
        print("Source Document:", chunk.metadata.get("source"))
        print("Page Number:", chunk.metadata.get("page_label"))
        print("Content:")
        print(chunk.page_content)
        print("\n")

    #Embedding the chunks
    embeddings = get_embedding()

    #Storing the embeddings in a vector database
    store_in_vectordb(chunks, embeddings)

if __name__ == "__main__":
    main()
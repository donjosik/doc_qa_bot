from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)

#query = "What are the function ai agents?"

#results = vectordb.similarity_search_with_score(
#    query,
#    k=5
#)

THRESHOLD = 0.7

def retrieve_docs(query):
    results = vectordb.similarity_search_with_score(
        query,
        k=3
    )

    relevant_docs = []

    for doc, score in results:
        print(doc.metadata.get("source"), doc.metadata.get("page"))
        #print(f"Score: {score}")
        #print(doc.page_content[:100])
        #print("-" * 50)

        if score < THRESHOLD:
            relevant_docs.append(doc)

    return relevant_docs
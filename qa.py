from retriever import retrieve_docs
from llm_service import generate_response

def main():
    print("QA BOT started")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            query = input("Ask a question: ")

            if query.lower() in ["exit", "quit"]:
                print("GoodBye!")
                break
            if not query:
                continue

            docs = retrieve_docs(query)

            context_parts = []
            for i,doc in enumerate(docs):
                source = doc.metadata.get("source", "Unknown")
                page = doc.metadata.get("page", "Unknown")

                print(f"\nChunk {i}")
                print(f"Source: {source}")
                print(f"Page: {page + 1 if page != 'Unknown' else page}")
                print("-" * 80)
                print(doc.page_content)
                print("-" * 80)

                context_parts.append(
                    f"""
                    "Source": {source}
                    "Page": {page + 1}
                    "Content": {doc.page_content}
                    """
                )

            context = "\n\n".join(context_parts)

            answer = generate_response(context=context, query=query)

            print("\nAnswer: ")
            print(answer)
        
        except KeyboardInterrupt:
            print("\n GoodBye!")
            break

if __name__ == "__main__":
    main()

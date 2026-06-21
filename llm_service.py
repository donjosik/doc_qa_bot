from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="llama3"
)

def generate_response(context, query):
    prompt = f"""
You are a document QA assistant.

Use ONLY the provided context.

Each context block contains:
- Source
- Page
- Content

When answering:
1. Find the answer from the Content.
2. Copy the corresponding Source and Page from the same block.
3. Include them in the Sources section.

If the answer is not found, respond exactly:

I don't know based on the provided documents.

Context:
{context}

Question:
{query}

"""
    print(prompt)
    response = llm.invoke(prompt)
    return response
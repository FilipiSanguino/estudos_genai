import os
import sys
import faiss
import numpy as np
from pypdf import PdfReader
import openai


def extract_text(path: str) -> str:
    reader = PdfReader(path)
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def chunk_text(text: str, size: int = 1000, overlap: int = 200):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += size - overlap
    return chunks


def embed(texts):
    response = openai.Embedding.create(input=texts, engine="text-embedding-ada-002")
    return [np.array(d["embedding"], dtype=np.float32) for d in response["data"]]


def build_index(chunks):
    embeddings = embed(chunks)
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.vstack(embeddings))
    return index, embeddings


def search(index, embeddings, chunks, query, k=1):
    q_emb = embed([query])[0]
    distances, indices = index.search(np.array([q_emb]), k)
    return chunks[indices[0][0]]


def generate_answer(context, question):
    prompt = f"Contexto:\n{context}\n\nPergunta: {question}\nResposta:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
    )
    return response.choices[0].text.strip()


def main():
    if len(sys.argv) < 3:
        print("Uso: python main.py <arquivo.pdf> <pergunta>")
        return
    pdf_path = sys.argv[1]
    question = sys.argv[2]

    text = extract_text(pdf_path)
    chunks = chunk_text(text)
    index, embeddings = build_index(chunks)
    context = search(index, embeddings, chunks, question)
    answer = generate_answer(context, question)
    print("Resposta:\n", answer)


if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        print("Defina a vari\u00e1vel OPENAI_API_KEY.")
        sys.exit(1)
    main()

import os
import sys
from pypdf import PdfReader
import openai


def extract_text(path: str) -> str:
    reader = PdfReader(path)
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def summarize(text: str) -> str:
    prompt = f"Resuma o texto a seguir:\n\n{text}\n"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
    )
    return response.choices[0].text.strip()


def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <arquivo.pdf>")
        return

    pdf_path = sys.argv[1]
    text = extract_text(pdf_path)
    resumo = summarize(text)
    print("Resumo:\n", resumo)


if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        print("Defina a vari\u00e1vel OPENAI_API_KEY.")
        sys.exit(1)
    main()

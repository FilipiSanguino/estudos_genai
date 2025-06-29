import os
import sys
import openai


def load_text(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()


def ask_question(context: str, question: str) -> str:
    prompt = f"Contexto:\n{context}\n\nPergunta: {question}\nResposta:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
    )
    return response.choices[0].text.strip()


def main():
    if len(sys.argv) < 3:
        print("Uso: python main.py <arquivo.txt> <pergunta>")
        return

    path = sys.argv[1]
    question = sys.argv[2]
    text = load_text(path)
    answer = ask_question(text, question)
    print("Resposta:\n", answer)


if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        print("Defina a vari\u00e1vel OPENAI_API_KEY.")
        sys.exit(1)
    main()

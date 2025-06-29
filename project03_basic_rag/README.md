# Project 03 - Basic RAG

Neste projeto construímos um pipeline simples de Retrieval-Augmented Generation.
Usaremos embeddings para indexar o texto de um PDF e responder perguntas sobre ele.

## Passos
1. Crie um ambiente virtual (opcional).
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Defina `OPENAI_API_KEY`.
4. Coloque o PDF desejado na pasta e execute:
   ```bash
   python main.py exemplo.pdf "Qual é o assunto principal?"
   ```

O script cria um índice vetorial simples e usa o trecho mais relevante para gerar
a resposta.

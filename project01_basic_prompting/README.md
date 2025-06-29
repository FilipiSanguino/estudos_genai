# Project 01 - Basic Prompting

Este é o ponto de partida mais simples. O objetivo é apenas enviar um texto
para um modelo de linguagem e receber uma resposta. Aqui usaremos a API da
OpenAI, mas você pode adaptar para outro provedor.

## Passos

1. Crie um ambiente virtual (opcional).
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Defina a variável de ambiente `OPENAI_API_KEY` com sua chave de API.
4. Execute o script principal:
   ```bash
   python main.py "arquivo.txt" "Pergunta sobre o texto"
   ```

O script lê o texto do arquivo, envia para o modelo e exibe a resposta no
terminal.

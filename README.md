# Chatbot de Normas de Segurança em Ambientes Industriais

Este é um projeto simples de chatbot desenvolvido para ajudar os usuários a obter informações sobre normas de segurança em ambientes industriais. O chatbot utiliza o modelo GPT-2 para gerar respostas baseadas em prompts fornecidos pelos usuários.

## Instalação

1. Clone o repositório:
   ```bash
  git clone https://github.com/riqueschilder/P4M8.git
   cd P4M8
Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
Instale as dependências:

pip install transformers gradio
##Execute o chatbot:

python chatbot.py
##Uso
O chatbot é uma interface de linha de comando simples. Insira um prompt relacionado às normas de segurança em ambientes industriais, e o chatbot responderá com informações geradas pelo modelo GPT-2.

Exemplo de prompt:

Quais são os requisitos para o uso de EPIs em uma fábrica?

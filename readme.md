# 🪲 Project Gregor – RAG Literário (Kafka)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-v0.3-green)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange)
![License](https://img.shields.io/badge/License-MIT-purple)

Sistema inteligente de **RAG (Retrieval-Augmented Generation)** projetado para analisar, indexar e conversar com obras literárias. A implementação atual utiliza o clássico *"A Metamorfose"* de Franz Kafka como base de conhecimento vetorial.

O projeto demonstra a aplicação prática de Engenharia de Dados e IA Generativa para busca semântica, recuperação de contexto e redução de alucinações.

---

## 2. Índice

1. [Índice](#2-índice)
2. [Visão Geral](#2-visão-geral)
3. [Pré-requisitos](#3-pré-requisitos)
4. [Instalação](#4-instalação)
5. [Uso](#5-uso)
6. [Configuração](#6-configuração)
7. [Estrutura do Projeto](#7-estrutura-do-projeto)
8. [Como Contribuir](#8-como-contribuir)
9. [Licença](#9-licença)

---

## 2. Visão Geral

Este projeto implementa um pipeline completo de dados (ETL + Inferência) para transformar um PDF não estruturado em uma base de conhecimento consultável.

### Principais Funcionalidades

* **🧠 Busca Semântica**
  Diferente da busca por palavra-chave (Ctrl+F), o sistema entende o *significado* da pergunta para encontrar trechos relevantes no livro.

* **📚 Citação de Fontes (Grounding)**
  Toda resposta gerada pela IA indica a **página exata** do PDF onde a informação foi encontrada, garantindo rastreabilidade.

* **🔪 Chunking Inteligente**
  Utiliza `RecursiveCharacterTextSplitter` para fatiar o texto respeitando a estrutura de parágrafos e frases, preservando o contexto.

* **💾 Persistência Vetorial**
  Os dados processados são salvos localmente no **ChromaDB**, eliminando a necessidade de reprocessar o documento a cada execução.

---

## 3. Pré-requisitos

* **OpenAI API Key** (Com créditos ativos)
* **Python 3.10+**
* **Git** (Para versionamento)
* **VS Code** (Recomendado)

---

## 4. Instalação

**1 - Clone o repositório**
```bash
git clone [https://github.com/SEU-USUARIO/project-gregor-rag.git](https://github.com/SEU-USUARIO/project-gregor-rag.git)
cd project-gregor-rag
```
**2 - Crie o ambiente virtual
```bash
    python -m venv venv
venv/scripts/activate
```
**3 - Instale as dependencias
```
    pip install -r requirements.txt
```

## 5. Uso

O projeto opera em dois modos: Ingestão (preparação) e Chat (interação).

1. Prepare os dados (Rode uma vez) Este script lê o PDF e cria o banco vetorial.
```
    python ingest.py
```

Saída esperada: "✅ Sucesso! Banco de dados criado."

2. Inicie o Chatbot Este script carrega o banco e inicia a conversa.
```
    python main.py
```

Exemplo de interação no terminal:
```
    Você: Qual foi a reação do pai ao ver o inseto?
    IA: O pai reagiu com hostilidade, empurrando Gregor de volta para o quarto com uma bengala e um jornal, batendo os pés violentamente...
    (Fonte: Página 19)
```

## 6. Configuração

Crie um arquivo .env na raiz do projeto contendo sua chave:

```
OPENAI_API_KEY=sk-proj-sua-chave-aqui...
```

Nota: Um arquivo de exemplo não é necessário pois a configuração é única, mas certifique-se de não commitar este arquivo.
import os
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader # <--- A novidade

load_dotenv()

def ingerir_livro():
    caminho_do_livro = r"C:\Users\colaborador\Documents\RAG\data\A-METAMORFOSE.pdf"

    print(f"Livro: '{caminho_do_livro}")
    loader = PyPDFLoader(caminho_do_livro)
    docs_brutos = loader.load()
    print(f"Livro carregado! Total de páginas: {len(docs_brutos)}")
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=100,
        separators=["\n\n", "\n", " ", ""]
    )
    docs_processados = text_splitter.split_documents(docs_brutos)
    print(f"Chuncks gerados: {len(docs_processados)}")

    if os.path.exists("./banco_dados_chroma"):
        print("Aviso: Atualizando banco existente...")
        
    Chroma.from_documents(
        documents=docs_processados,
        embedding=OpenAIEmbeddings(),
        persist_directory="./banco_dados_chroma"
    )
    print("Livro indexado")

if __name__ == "__main__":
    ingerir_livro()
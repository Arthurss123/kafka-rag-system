import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def perguntar(query):
    vector_db = Chroma(
        persist_directory="./banco_dados_chroma", 
        embedding_function=OpenAIEmbeddings()
    )
    
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    prompt = ChatPromptTemplate.from_template("""
    Você é um assistente que responde perguntas baseadas APENAS no contexto abaixo.
    Se a resposta não estiver no contexto, diga que não sabe.
    
    <contexto>
    {context}
    </contexto>

    Pergunta: {input}
    """)

    document_chain = create_stuff_documents_chain(llm, prompt)

    retriever = vector_db.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    response = retrieval_chain.invoke({"input": query})
    
    resposta_texto = response['answer']
    fontes = response.get('context', [])

    if fontes:
        pagina = fontes[0].metadata.get('page_label') or fontes[0].metadata.get('page')
        if isinstance(pagina, int):
            pagina += 1
        return f"{resposta_texto}\n\n(Fonte: Página {pagina})"
    
    return resposta_texto

if __name__ == "__main__":
    print("--- Chatbot Kafka (Versão Moderna v1+) ---")
    while True:
        user_input = input("\nVocê: ")
        if user_input.lower() in ['sair', 'exit']:
            break
        
        try:
            resp = perguntar(user_input)
            print(f"IA: {resp}")
        except Exception as e:
            print(f"Erro detalhado: {e}")
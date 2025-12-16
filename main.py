import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def perguntar(query):
    # 1. Carregar o banco
    vector_db = Chroma(
        persist_directory="./banco_dados_chroma", 
        embedding_function=OpenAIEmbeddings()
    )
    
    # 2. Configurar o LLM
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # 3. Criar o Prompt (Agora é obrigatório definir como a IA deve agir)
    prompt = ChatPromptTemplate.from_template("""
    Você é um assistente que responde perguntas baseadas APENAS no contexto abaixo.
    Se a resposta não estiver no contexto, diga que não sabe.
    
    <contexto>
    {context}
    </contexto>

    Pergunta: {input}
    """)

    # 4. Criar a "Corrente de Documentos" (Combina os textos achados com o prompt)
    document_chain = create_stuff_documents_chain(llm, prompt)

    # 5. Criar a "Corrente de Recuperação" (Conecta o banco vetorial com a corrente acima)
    retriever = vector_db.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    # 6. Executar
    # Note que agora passamos "input" em vez de "query"
    response = retrieval_chain.invoke({"input": query})
    
    # Tratamento para mostrar a fonte (página)
    resposta_texto = response['answer']
    fontes = response.get('context', [])

    if fontes:
        # Pega a página da primeira fonte (tratando erros de metadados)
        pagina = fontes[0].metadata.get('page_label') or fontes[0].metadata.get('page')
        # Ajuste se for número inteiro (começa do 0, vira 1)
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
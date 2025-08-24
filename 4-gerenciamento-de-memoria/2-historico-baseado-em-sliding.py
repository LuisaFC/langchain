from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.messages import trim_messages
from langchain_core.runnables import RunnableLambda

load_dotenv()

# Define que o assistente deve responder com piadas curtas
prompt = ChatPromptTemplate.from_messages([
    ("system", "You're a helpful assistant that answers with a short joke when possible."),
    MessagesPlaceholder("history"),
    ("human", "{input}"),
])

# Inicializa o modelo
llm = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")

# Prepara as entradas para o modelo
def prepare_inputs(payload: dict) -> dict:
    # Obtém o histórico completo
    raw_history = payload.get("raw_history", [])
    # Corta o histórico para manter apenas as últimas mensagens relevantes
    trimmed = trim_messages(
        raw_history,
        token_counter=len,
        max_tokens=2,
        strategy="last",
        start_on="human",
        include_system=True,
        allow_partial=False,
    )
    return {"input": payload.get("input",""), "history": trimmed}

# Transforma a função prepare_inputs em um Runnable
prepare = RunnableLambda(prepare_inputs)

# Cria a chain com o prepare, o prompt e o modelo
chain = prepare | prompt | llm

# Cria um gerenciador de histórico de mensagens em memória
session_store: dict[str, InMemoryChatMessageHistory] = {}

# Cria uma função para obter o histórico da sessão
# Cada sessão tem seu próprio histórico independente
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

# Cria a chain com o histórico
conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="raw_history"
)

# Configura a sessão com o id da sessão
config = {"configurable": {"session_id": "demo-session"}}

# Invoca a chain com diferentes perguntas
resp1 = conversational_chain.invoke({"input": "My name is Luisa. Reply only with 'OK' and do not mention my name."}, config=config)
print("Assistant:", resp1.content)

resp2 = conversational_chain.invoke({"input": "Tell me a one-sentence fun fact. Do not mention my name."}, config=config)
print("Assistant:", resp2.content)

resp3 = conversational_chain.invoke({"input": "What is my name?"}, config=config)
print("Assistant:", resp3.content)
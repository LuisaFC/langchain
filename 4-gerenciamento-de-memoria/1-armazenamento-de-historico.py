from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory

load_dotenv()

# Cria o prompt com o sistema, o histórico e o input
# Inicia o chat com o sistema, depois carrega o histórico e depois carrega o input
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}"),
])

# Inicializa o modelo
chat_model = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")

# Cria a chain com o prompt e o modelo
chain = prompt | chat_model

# Cria um gerenciador de histórico de mensagens em memória
session_store: dict[str, InMemoryChatMessageHistory] = {}

# Cria uma função para obter o histórico da sessão
# Cada sessão tem seu próprio histórico independente
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]

# Cria a chain com o histórico
# RunnableWithMessageHistory é uma classe que permite criar uma chain com um histórico de mensagens
# get_session_history é a função que obtém o histórico da sessão
# input_messages_key é a chave do input
# history_messages_key é a chave do histórico
conversational_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# Configura a sessão com o id da sessão
config = {"configurable": {"session_id": "demo-session"}}

# Interactions
response1 = conversational_chain.invoke({"input": "Hello, my name is Luisa. how are you?"}, config=config)
print("Assistant: ", response1.content)
print("-"*30)

response2 = conversational_chain.invoke({"input": "Can you repeat my name?"}, config=config)
print("Assistant: ", response2.content)
print("-"*30)

response3 = conversational_chain.invoke({"input": "Can you repeat my name in a motivation phrase?"}, config=config)
print("Assistant: ", response3.content)
print("-"*30)
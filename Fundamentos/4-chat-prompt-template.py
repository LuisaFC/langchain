from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#Cria o system -> como o modelo deve se comportar
system = ("systems", "You are a helpful assistant that can answer questions in a {style} style")
# Cria o user -> a pergunta do usuario
user = ("user", "{question}")

#cria o template com o system e o user
chat_prompt = ChatPromptTemplate.from_messages([system, user])

# formata o template com o system e o user
messages = chat_prompt.format_messages(style="formal", question="What is the capital of France?")

# mostra a mensagem formatada
for message in messages:
    print(message)

# Cria o modelo com parametros
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# Invoca o modelo com a mensagem formatada
response = model.invoke(messages)

# mostra a resposta do modelo para a pergunta do usuario
print(response.content)
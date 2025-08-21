# Biblioteca para criar o modelo OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

#carrega as variaveis de ambiente
load_dotenv()

#cria o LLM com o modelo gpt-4o-mini e temperatura 0.5
model = ChatOpenAI(model="gpt-5-nano", temperature=0.5)

#Envia mensagem para o modelo
message = model.invoke("Hello, world!")

#printa a resposta do modelo
print(message.content)

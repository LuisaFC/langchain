# Biblioteca generica para criar o modelo de chat
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

#carrega as variaveis de ambiente
load_dotenv()

#cria o modelo  
gemini = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")

#Envia mensagem para o modelo
answer = gemini.invoke("Hello, world!")

#printa a resposta do modelo
print(answer.content)
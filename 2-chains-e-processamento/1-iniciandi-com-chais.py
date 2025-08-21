from langchain.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

# Cria o template com o input_variables e a template
question_template = PromptTemplate(
    input_variables=["name"],
    template="Hello, I am {name}! Tell me a joke with my name"
)

# Cria o modelo com parametros
model = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")

# Após criar o template dinamicamente, o template é passado para o modelo
chain = question_template | model

# Invoca a chain com o input    
response = chain.invoke({"name": "John"})

# mostra a resposta do modelo para a pergunta do usuario
print(response.content)
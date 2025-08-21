from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Cria o template com o input_variables e a template
question_template = PromptTemplate(
    input_variables=["name"],
    template="Hello, I am {name}! Tell me a joke with my name"
)

# Cria o modelo com parametros
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

# Após criar o template dinamicamente, o template é passado para o modelo
chain = question_template | model

# Invoca a chain com o input    
response = chain.invoke({"name": "John"})

# mostra a resposta do modelo para a pergunta do usuario
print(response.content)
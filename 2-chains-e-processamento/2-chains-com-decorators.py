from langchain.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from langchain_core.runnables import chain
from dotenv import load_dotenv

load_dotenv()

# Cria uma chain com o decorator @chain
@chain
def square(input_dict:dict) -> dict:
    x = input_dict["x"]
    return {"square_result": x * x}

# Cria o template com o input_variables e a template
question_template2 = PromptTemplate(
    input_variables=["square_result"],
    template="Tell me about the number {square_result}"
)

# Cria o modelo com parametros
model = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")

# Fluxo de trabalho
chain = square | question_template2 | model

# Invoca a chain com o input   
response = chain.invoke({"x": 10})

# mostra a resposta do modelo para a pergunta do usuario
print(response.content)
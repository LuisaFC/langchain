from langchain.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# Cria template com variaveis
template_translate = PromptTemplate(
    input_variables=["initial_text"],
    template="Translate the following text to English: \n ```{initial_text}```"
)

template_summary = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in 4 words: \n ```{text}```\n\n"
)

# Cria o modelo
llm_en = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai")

# pipeline de processamento
translate = template_translate | llm_en | StrOutputParser()
pipeline = {"text": translate} | template_summary | llm_en | StrOutputParser()

# O StrOutputParser() é um parser de saída que converte a resposta do modelo de linguagem (LLM) em uma string simples.

result = pipeline.invoke({"initial_text": "LangChain é um framework para desenvolvimento de aplicações de IA"})
print(result)
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#cria o sistema e o usuario
system = ("systems", "You are a helpful assistant that can answer questions in a {style} style")
user = ("user", "{question}")

#cria o prompt
chat_prompt = ChatPromptTemplate.from_messages([system, user])

messages = chat_prompt.format_messages(style="formal", question="What is the capital of France?")

for message in messages:
    print(message)

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)

response = model.invoke(messages)

print(response.content)
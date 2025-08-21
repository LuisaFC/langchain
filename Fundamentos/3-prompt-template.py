from langchain.prompts import PromptTemplate

#cria o template com o input_variables e a template
template = PromptTemplate(
    input_variables=["name"],
    template="Hello, I am {name}! Tell me a joke with my name"
)

# formata o template com o input_variables
text = template.format(name="John")

print(text)
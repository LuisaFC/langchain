from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Carrega o arquivo pdf
loader = PyPDFLoader("./gpt5.pdf")

# Armazena os documentos carregados
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

chunks = splitter.split_documents(docs)

print(len(chunks))
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Carrega o site da LangChain
loader = WebBaseLoader("https://www.langchain.com/")

# Armazena os documentos carregados
docs = loader.load()

# Divide os documentos em chunks
# chunks de 500 tokens
# overlap de 100 tokens
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

# Divide os documentos em chunks
chunks = splitter.split_documents(docs)

for chunk in chunks:
    print(chunk)
    print("-"*30)
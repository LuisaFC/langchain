import os
from pathlib import Path
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from langchain_postgres import PGVector

load_dotenv()
# Verifica se as variáveis de ambiente estão configuradas
for k in ("GOOGLE_API_KEY", "PGVECTOR_URL","PGVECTOR_COLLECTION"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

# Localiza o arquivo pdf
current_dir = Path(__file__).parent
pdf_path = current_dir / "gpt5.pdf"

# Carrega o arquivo pdf
docs = PyPDFLoader(str(pdf_path)).load()

# Define o tamanho dos chunks e o overlap
splits = RecursiveCharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=150, add_start_index=False).split_documents(docs)
# Verifica se os chunks foram criados
if not splits:
    raise SystemExit(0)

# Limpa os metadados do documento
enriched = [
    Document(
        page_content=d.page_content,
        metadata={k: v for k, v in d.metadata.items() if v not in ("", None)}
    )
    for d in splits
]    
# Cria os ids para os documentos
ids = [f"doc-{i}" for i in range(len(enriched))]

# Configura o modelo de embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Estabelece a conexão com o banco de dados
store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

# Adiciona os documentos ao banco de dados
store.add_documents(documents=enriched, ids=ids)

# Cria os ids para os documentos
# enriched = []
# for d in splits:
#     meta = {k: v for k, v in d.metadata.items() if v not in ("", None)}
#     new_doc = Document(
#         page_content=d.page_content,
#         metadata=meta
#     )
#     enriched.append(new_doc)
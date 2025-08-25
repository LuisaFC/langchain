import os
from dotenv import load_dotenv
from langchain_postgres import PGVector
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

# Configura o modelo de embeddings (mesmo usado na ingestão)
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Conecta ao banco
store = PGVector(
    embeddings=embeddings,
    collection_name=os.getenv("PGVECTOR_COLLECTION"),
    connection=os.getenv("PGVECTOR_URL"),
    use_jsonb=True,
)

print("🔍 EXPLORANDO O BANCO DE DADOS VETORIAL")
print("=" * 50)

# 1. Informações básicas
print(f"\n📊 ESTATÍSTICAS:")
print(f"   • Total de documentos: {store._collection.count()}")

# 2. Ver alguns documentos
print(f"\n📄 AMOSTRA DE DOCUMENTOS:")
docs = store._collection.get()
for i, doc in enumerate(docs['documents'][:3]):  # Primeiros 3 documentos
    print(f"\n   Documento {i+1}:")
    print(f"   ID: {docs['ids'][i]}")
    print(f"   Conteúdo: {doc[:200]}...")
    print(f"   Metadados: {docs['metadatas'][i]}")

# 3. Ver metadados únicos
print(f"\n🏷️  METADADOS DISPONÍVEIS:")
if docs['metadatas']:
    sample_metadata = docs['metadatas'][0]
    for key, value in sample_metadata.items():
        print(f"   • {key}: {value}")

# 4. Busca simples
print(f"\n🔎 TESTE DE BUSCA:")
query = "GPT-5 capabilities"
print(f"   Buscando por: '{query}'")
results = store.similarity_search(query, k=2)
for i, result in enumerate(results):
    print(f"\n   Resultado {i+1}:")
    print(f"   Conteúdo: {result.page_content[:150]}...")
    print(f"   Metadados: {result.metadata}")

print(f"\n✅ Banco de dados explorado com sucesso!")

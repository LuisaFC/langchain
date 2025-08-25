# 🚀 LangChain - Study and Experimentation Project

This repository contains a comprehensive collection of practical examples and tutorials about LangChain, a Python library for building applications with Large Language Models (LLMs).

## 📚 About the Project

This project was developed as part of LangChain studies and serves as a practical guide for developers who want to learn how to implement different functionalities using LLMs. Each directory contains specific and functional examples that demonstrate important concepts of the LangChain ecosystem.

## 🏗️ Project Structure

```
LangChain/
├── Fundamentos/                           # Basic LangChain concepts
│   ├── 1-hello-world.py                  # First contact with LangChain
│   ├── 2-init-chat-model.py              # Chat model initialization
│   ├── 3-prompt-template.py              # Prompt templates
│   └── 4-chat-prompt-template.py         # Chat prompt templates
│
├── 2-chains-e-processamento/             # Processing chains
│   ├── 1-iniciandi-com-chais.py         # Introduction to chains
│   ├── 2-chains-com-decorators.py       # Chains using decorators
│   ├── 3-runnable-lambda.py              # Lambda executables
│   ├── 4-pipeline-de-processament.py     # Processing pipelines
│   ├── 5-sumarizacao.py                  # Text summarization
│   ├── 6-sumarizacao-map-reducer.py      # MapReduce summarization
│   └── 7-pipeline-de-sumarizacao.py      # Complete summarization pipeline
│
├── 3-agentes-e-tools/                     # Agents and tools
│   ├── 1-agente-react-e-tools.py         # ReAct agent with tools
│   └── 2-agente-react-usando-prompt-hub.py # Agent using Prompt Hub
│
├── 4-gerenciamento-de-memoria/           # Memory management
│   ├── 1-armazenamento-de-historico.py   # Conversation history storage
│   └── 2-historico-baseado-em-sliding.py # Sliding window history
│
├── 5-loaders-e-banco-de-dados-vetoriais/ # Loaders and vector databases
│   ├── 1-carregamento-usando-WebBaseLoader.py # Web page loading
│   ├── 2-carregamento-de-pdf.py          # PDF loading
│   ├── 3-ingestion-pgvector.py           # Data ingestion in pgvector
│   ├── 4-search-vector.py                # Vector search
│   ├── 4-view-database.py                # Database visualization
│   └── gpt5.pdf                          # Example document
│
├── docker-compose.yaml                    # PostgreSQL + pgvector configuration
├── config.env.example                     # Environment variables example
├── requirements.txt                       # Python dependencies
└── README.md                             # This file
```

## 🚀 Main Features

### 🔧 Fundamentals
- **Hello World**: First contact with LangChain
- **Chat Models**: Configuration and use of different LLMs
- **Prompt Templates**: Creation of structured and reusable prompts

### ⛓️ Chains and Processing
- **Basic Chains**: Fundamental concepts of processing chains
- **Decorators**: Using decorators to simplify chains
- **Pipelines**: Building complex processing flows
- **Summarization**: Different approaches for text summarization
- **MapReduce**: Parallel and distributed processing

### 🤖 Agents and Tools
- **ReAct Agent**: Implementation of the ReAct pattern (Reasoning + Acting)
- **Prompt Hub**: Using Prompt Hub for predefined prompts
- **Tools**: Integration of different tools with agents

### 🧠 Memory Management
- **History**: Storage and retrieval of conversations
- **Sliding Window**: Memory with sliding window for optimization

### 📊 Vector Databases
- **Loaders**: Different types of loaders (Web, PDF)
- **pgvector**: Integration with PostgreSQL + pgvector
- **Vector Search**: Implementation of similarity search
- **Ingestion**: Complete document ingestion process

## 🛠️ Technologies Used

- **Python 3.10+**
- **LangChain**: Main framework for LLMs
- **PostgreSQL + pgvector**: Vector database
- **Docker & Docker Compose**: Containerization
- **Google Gemini API**: Embedding model and LLM
- **OpenAI API**: Alternative for LLMs (configurable)

## 📋 Prerequisites

- Python 3.10 or higher
- Docker and Docker Compose
- Google AI account (for Gemini) or OpenAI
- Git

## 🚀 Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd LangChain
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
```bash
cp config.env.example .env
# Edit the .env file with your credentials
```

### 5. Start the database
```bash
docker-compose up -d
```

## ⚙️ Configuration

### Environment Variables (.env)

```bash
# Google Gemini API
GOOGLE_API_KEY=your_gemini_api_key_here

# PostgreSQL with pgvector
PGVECTOR_URL=postgresql://postgres:postgres@localhost:5432/rag
PGVECTOR_COLLECTION=documents

# OpenAI (alternative)
# OPENAI_API_KEY=your_openai_api_key_here
# OPENAI_MODEL=gpt-4
```

### Database

The project includes a `docker-compose.yaml` that configures:
- **PostgreSQL 17** with pgvector extension
- **pgAdmin** for administration (port 8080)
- **Vector extension** automatically installed

## 📖 How to Use

### Basic Examples

1. **Fundamentals**:
   ```bash
   python Fundamentos/1-hello-world.py
   python Fundamentos/2-init-chat-model.py
   ```

2. **Chains**:
   ```bash
   python 2-chains-e-processamento/1-iniciandi-com-chais.py
   python 2-chains-e-processamento/5-sumarizacao.py
   ```

3. **Agents**:
   ```bash
   python 3-agentes-e-tools/1-agente-react-e-tools.py
   ```

4. **Vector Database**:
   ```bash
   python 5-loaders-e-banco-de-dados-vetoriais/4-search-vector.py
   ```

### Typical Workflow

1. **Load documents**: Use loaders to load PDFs, web pages, etc.
2. **Process with LangChain**: Apply chains, agents, or pipelines
3. **Store vectors**: Save embeddings in the vector database
4. **Search and retrieve**: Implement similarity search
5. **Manage memory**: Maintain context between sessions

## 🔍 Usage Examples

### Document Summarization
```python
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_postgres import PGVector

# Configure embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Search similar documents
store = PGVector(
    embeddings=embeddings,
    collection_name="documents",
    connection=os.getenv("PGVECTOR_URL")
)

results = store.similarity_search("your query here", k=3)
```

### Agent with Tools
```python
from langchain.agents import AgentExecutor, create_react_agent
from langchain.tools import Tool

# Create tools
tools = [
    Tool(
        name="search",
        func=search_function,
        description="Search for information on the web"
    )
]

# Create agent
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)
```

## 🐛 Troubleshooting

### Database Connection Error
- Check if Docker is running: `docker ps`
- Confirm credentials in the `.env` file
- Restart containers: `docker-compose restart`

### API Key Error
- Verify that the `GOOGLE_API_KEY` variable is configured
- Confirm that the key is valid and has adequate permissions

### Dependencies
- Activate the virtual environment: `source venv/bin/activate`
- Reinstall dependencies: `pip install -r requirements.txt`

## 📚 Additional Resources

- [Official LangChain Documentation](https://python.langchain.com/)
- [Google AI Studio](https://aistudio.google.com/)
- [PostgreSQL + pgvector](https://github.com/pgvector/pgvector)
- [Docker Documentation](https://docs.docker.com/)

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is under the MIT license. See the `LICENSE` file for more details.

## 👨‍💻 Author

Developed as part of LangChain and LLM studies.

---

⭐ **If this project was useful to you, consider giving it a star!**

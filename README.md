
<img width="1920" height="1080" alt="Screenshot (41)" src="https://github.com/user-attachments/assets/04e52ec3-a9fd-4c7c-a88f-5f26580d453f" />

# Insurance AI Platform

description: |
  Insurance AI Platform is a comprehensive AI-powered system designed to provide insights and support across multiple insurance operations. It integrates chatbots, AI agents, document retrieval, SQL query handling, summarization, and knowledge graph querying to assist insurance professionals and customers efficiently.

project_structure: |
  Insurance-AI-Platform/
  │
  ├─ Data/
  │   ├─ insurance.db             # SQLite database with sample insurance data
  │   └─ sample_policy.pdf        # Sample health insurance policy document
  │
  ├─ Modules/
  │   ├─ task1_chatbot.py         # Chatbot module
  │   ├─ task2_ai_agent.py        # AI Agent / Calculator module
  │   ├─ task3_rag_basic.py       # Knowledge Retriever (RAG Basic) module
  │   ├─ task4_rag_memory.py      # Policy Advisor (RAG Memory) module
  │   ├─ task5_sql_qa.py          # SQL Query module
  │   ├─ task6_summarizer.py      # Document Summarization module
  │   └─ task7_graph_qa.py        # Graph QA module (Neo4j)
  │
  ├─ SQL_DATA_CREATION/
  │   ├─ CreateDB.py              # Script to create SQLite database tables
  │   └─ add_SQLdata.py           # Script to populate sample data into database
  │
  ├─ app.py                       # Streamlit main app
  ├─ .env                         # Environment variables for database and APIs
  ├─ requirements.txt             # Python dependencies
  └─ README.md                    # Project documentation

modules: |
  1. Chatbot
     - Natural language interface for general insurance queries.
     - Stores session history.
  2. Calculator (AI Agent)
     - Performs policy calculations or AI agent tasks.
  3. Knowledge Retriever (RAG Basic)
     - Retrieves information from uploaded PDFs.
  4. Policy Advisor (RAG Memory)
     - Multi-step question answering with context retention.
  5. SQL QA
     - Query SQLite insurance database (`insurance.db`) using natural language.
  6. Summarization
     - Summarizes policy documents or other uploaded text.
  7. Graph QA (Neo4j)
     - Queries knowledge graph of insurance entities: Customer, Policy, Claim, RiskEvent, FraudFlag.

setup_instructions: |
  1. Clone the repository:
     git clone <your-repo-url>
     cd Insurance-AI-Platform

  2. Create and activate virtual environment:
     python -m venv venv
     source venv/bin/activate   # Linux / macOS
     venv\Scripts\activate      # Windows

  3. Install dependencies:
     pip install -r requirements.txt

  4. Setup environment variables in `.env`:
     DB_PATH=./Data/insurance.db
     NEO4J_URI=bolt://<your-neo4j-host>:7687
     NEO4J_USERNAME=<your-username>
     NEO4J_PASSWORD=<your-password>
     GROQ_API_KEY=<your-groq-api-key>

  5. Initialize database:
     python SQL_DATA_CREATION/CreateDB.py
     python SQL_DATA_CREATION/add_SQLdata.py

  6. Run the Streamlit app:
     streamlit run app.py

usage: |
  - Select the module from the sidebar.
  - Enter your query or input in the text area.
  - Click "Submit" to get results.
  - For modules with chat history (Chatbot, Knowledge Retriever, Policy Advisor, Graph QA), you can clear the chat history using the "Clear Chat History" button.

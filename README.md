
<img width="1920" height="1080" alt="Screenshot (41)" src="https://github.com/user-attachments/assets/04e52ec3-a9fd-4c7c-a88f-5f26580d453f" />

# Insurance AI Platform

## Description
Insurance AI Platform is a comprehensive AI-powered system designed to provide insights and support across multiple insurance operations.  
It integrates chatbots, AI agents, document retrieval, SQL query handling, summarization, and knowledge graph querying to assist insurance professionals and customers efficiently.

<img width="592" height="721" alt="image" src="https://github.com/user-attachments/assets/8f0346af-07c5-45d7-82c4-8053822c7b2e" />



---

## Modules

1. **Chatbot**
   - Natural language interface for general insurance queries.
   - Stores session history for ongoing conversations.

2. **Calculator (AI Agent)**
   - Performs policy calculations or AI agent tasks.
   - Executes multi-step queries.

3. **Knowledge Retriever (RAG Basic)**
   - Retrieves information from uploaded PDFs.
   - Stores session history.

4. **Policy Advisor (RAG Memory)**
   - Multi-step question answering with context retention.
   - Stores session history.

5. **SQL QA**
   - Query SQLite insurance database (`insurance.db`) using natural language.

6. **Summarization**
   - Summarizes policy documents or other uploaded text.

7. **Graph QA (Neo4j)**
   - Queries knowledge graph of insurance entities:
     Customer, Policy, Claim, RiskEvent, FraudFlag.
   - Stores session history.

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Insurance-AI-Platform
2. **Create and active virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate      # Windows
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Setup environment variables**
   ```bash
   # Neo4j connection
   NEO4J_URI=bolt://<your-neo4j-host>:7687
   NEO4J_USERNAME=<your-username>
   NEO4J_PASSWORD=<your-password>

   # Groq API key (if using AI modules)
   GROQ_API_KEY=<your-groq-api-key>
5. **Initialize database*
   ```bash
   python SQL_DATA_CREATION/CreateDB.py
   python SQL_DATA_CREATION/add_SQLdata.py
6. **Run the Streamlit app**
    ```bash
    streamlit run app.py


Usage:
  - Select the module from the sidebar.
  - Enter your query or input in the text area.
  - Click Submit to get results.
  - For modules with chat history:
      - Chatbot
      - Knowledge Retriever
      - Policy Advisor
      - Graph QA
    - You can clear the chat history using the "Clear Chat History" button.

Data_Files:
  - insurance.db: "SQLite database containing sample insurance data (Customers, Policies, Claims, etc.)"
  - sample_policy.pdf: "Example insurance policy document used for RAG modules"

Notes:
  - Only modules that store chat history will show the "Clear Chat History" button.
  - SQL QA module interacts with the SQLite database.
  - Graph QA module requires Neo4j credentials in .env.
  - Ensure GROQ_API_KEY is set for AI modules.


Example_Queries:
  Chatbot:
  
    - "What does my health insurance policy cover?"
    - "How can I file a claim for car accident damages?"
    - "Explain the claim settlement process for hospitalization."
  Knowledge_Retriever:
  
    - "Give details about the Sample Health Insurance Policy."
    - "What are the exclusions in my policy?"
    - "List the coverage details for outpatient medical consultations."
  Policy_Advisor:
  
    - "Compare basic vs full coverage for car insurance."
    - "What benefits do I get if I opt for maternity coverage?"
    - "Suggest the best policy for frequent hospitalization needs."
  SQL_QA:
  
    - "SELECT * FROM Customers WHERE age > 40;"
    - "How many claims were filed in 2024?"
    - "List all policies of type 'Health' with coverage 'Basic'."
  Summarization:
  
    - "Summarize the Sample Health Insurance Policy."
    - "Give a brief overview of exclusions and claim process."
 
  
  Graph_QA:
  
    - MATCH (c:Customer)-[:FILED]->(cl:Claim)
      WHERE cl.amount > 10000
      RETURN c.name AS customer, cl.amount AS claim_amount

    - MATCH (c:Customer)-[:HOLDS]->(p:Policy)
      RETURN c.name, collect(p.type) AS policies

     - MATCH (cl:Claim)-[:ASSOCIATED_WITH]->(r:RiskEvent)
       RETURN cl.claim_id, r.description, r.risk_level
Tip: You can input either fully-written Cypher queries or rely on natural language (if using LLM integration).

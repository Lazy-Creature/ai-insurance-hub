# task5_sql_qa.py
import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_groq import ChatGroq

# -------------------- Load Environment --------------------
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
DB_PATH = "insurance.db"  # path to your SQLite database

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

# -------------------- Initialize LLM --------------------
llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.1-8b-instant")  # Use a valid model

# -------------------- Connect to Database --------------------
# Include all three tables: customers, claims, policies
db = SQLDatabase.from_uri(
    f"sqlite:///{DB_PATH}",
    include_tables=["customers", "claims", "policies"]
)

# -------------------- SQL Chain --------------------
sql_chain = SQLDatabaseChain.from_llm(
    llm=llm,
    db=db,
    verbose=True,        # enable logs
    return_direct=True   # return only SQL results
)

# -------------------- Query Function --------------------
def query_sql(question: str):
    """
    Run a natural language question against the insurance SQLite database.
    Example:
    - "Show the top 5 customers with highest claim amounts in the last 6 months."
    - "List all policies with coverage_amount greater than 100000."
    """
    if not question.strip():
        return "Please enter a question."

    try:
        result = sql_chain.run(question)

        if not result:
            return "No result returned."
        return result
    except Exception as e:
        return f"Error in SQL QA: {e}"

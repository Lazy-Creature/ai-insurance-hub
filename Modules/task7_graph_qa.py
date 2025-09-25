# task7_graph_qa.py
import os
import streamlit as st
from neo4j import GraphDatabase
from dotenv import load_dotenv

# Load credentials
load_dotenv()
NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

if not all([NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD]):
    raise ValueError("Neo4j credentials missing in .env file!")

# Initialize Neo4j driver once
_driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def run_cypher_query(query: str):
    """Run any Cypher query and return a list of dicts."""
    with _driver.session() as session:
        result = session.run(query)
        return [record.data() for record in result]

def handle_graph_qa_interaction(user_query: str):
    """Streamlit wrapper to handle Graph QA input and history."""
    
    if "graph_qa_history" not in st.session_state:
        st.session_state.graph_qa_history = []

    if user_query:
        try:
            results = run_cypher_query(user_query)
            st.session_state.graph_qa_history.append({
                "input": user_query,
                "output": results
            })
        except Exception as e:
            st.session_state.graph_qa_history.append({
                "input": user_query,
                "output": f"Error: {e}"
            })

    st.write("**Graph QA Chat History:**")
    for i, chat in enumerate(st.session_state.graph_qa_history, 1):
        st.markdown(f"**{i}. Input:** {chat['input']}")
        if isinstance(chat['output'], list):
            st.json(chat['output'])
        else:
            st.markdown(f"**Output:** {chat['output']}")

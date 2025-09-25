# app.py
import streamlit as st
import pandas as pd
from langchain.docstore.document import Document

from task1_chatbot import ask_chatbot
from task2_ai_agent import run_agent
from task3_rag_basic import query_documents
from task4_rag_memory import multi_step_query
from task5_sql_qa import query_sql
from task6_summarizer import summarize_documents
from task7_graph_qa import handle_graph_qa_interaction  # Graph QA

st.title("Insurance AI Platform")

# Sidebar module selection
st.sidebar.title("Modules")
module = st.sidebar.selectbox(
    "Choose Module",
    ["Chatbot", "Calculator", "Knowledge Retriever", "Policy Advisor", "SQL QA", "Summarization", "Graph QA"]
)

query = st.text_area("Enter your question or input:")

# Modules that keep chat history
session_modules = ["Chatbot", "Knowledge Retriever", "Policy Advisor", "Graph QA"]

# Initialize session states for modules that store chat
for mod in session_modules:
    key = f"{mod.lower().replace(' ', '_')}_history"
    if key not in st.session_state:
        st.session_state[key] = []

# Function to display chat history
def display_chat(history, module_name):
    st.write(f"**{module_name} Chat History:**")
    for i, chat in enumerate(history, 1):
        st.markdown(f"**{i}. Input:** {chat['input']}")
        if isinstance(chat['output'], dict) or isinstance(chat['output'], list):
            st.markdown(f"**Output:**")
            st.json(chat['output'])
        else:
            st.markdown(f"**Output:** {chat['output']}")

# Submit button
if st.button("Submit"):
    if not query or not query.strip():
        st.warning("Please enter a question first.")
    else:
        try:
            # ---------------- Chatbot Module ----------------
            if module == "Chatbot":
                response = ask_chatbot(query)
                st.session_state.chatbot_history.append({"input": query, "output": response})
                display_chat(st.session_state.chatbot_history, "Chatbot")

            # ---------------- Agent Module ----------------
            elif module == "Calculator":
                result = run_agent(query)
                st.write("**Agent Result:**")
                st.write(result)

            # ---------------- Knowledge Retriever Module ----------------
            elif module == "Knowledge Retriever":
                result = query_documents(query)
                st.session_state.knowledge_retriever_history.append({"input": query, "output": result})
                display_chat(st.session_state.knowledge_retriever_history, "Knowledge Retriever")

            # ---------------- Policy Advisor Module ----------------
            elif module == "Policy Advisor":
                result = multi_step_query(query)
                st.session_state.policy_advisor_history.append({"input": query, "output": result})
                display_chat(st.session_state.policy_advisor_history, "Policy Advisor")

            # ---------------- SQL QA Module ----------------
            elif module == "SQL QA":
                result = query_sql(query)
                st.subheader("SQL QA Result")
                st.write("**Raw Output:**")
                st.code(str(result))

                if isinstance(result, list):
                    try:
                        df = pd.DataFrame(result)
                        st.dataframe(df)
                    except Exception:
                        st.write(result)
                elif isinstance(result, dict):
                    st.json(result)

            # ---------------- Summarization Module ----------------
            elif module == "Summarization":
                st.subheader("Summarization Result")
                doc = [Document(page_content=query)]
                st.write(summarize_documents(doc))

            # ---------------- Graph QA Module ----------------
            elif module == "Graph QA":
                st.subheader("Graph QA Result")
                handle_graph_qa_interaction(query)
                
        except Exception as e:
            st.error(f"Error in {module}: {e}")

# ------------------- Clear Chat History Button -------------------
if module in session_modules:
    if st.button("Clear Chat History"):
        key = f"{module.lower().replace(' ', '_')}_history"
        st.session_state[key] = []  # clear only this module's chat
        st.success(f"{module} chat history cleared.")

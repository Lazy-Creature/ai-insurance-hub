# task3_rag_basic.py
import os
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.1-8b-instant")

# Load documents
loader = PyPDFLoader("sample_policy.pdf")
docs = loader.load()

# Embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # ⚡ pass object, do NOT call ()

# FAISS vectorstore
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever()

# RetrievalQA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

# Query function
def query_documents(question: str) -> str:
    if not question or not question.strip():
        return "Please enter a question."
    return qa.run(question)

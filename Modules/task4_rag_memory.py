# task4_rag_memory.py
import os
from dotenv import load_dotenv
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# -------------------------
# Memory for conversational RAG
# -------------------------
memory = ConversationBufferMemory(input_key="input", memory_key="history")

# -------------------------
# LLM
# -------------------------
llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.1-8b-instant")

# -------------------------
# Load documents
# -------------------------
loader = PyPDFLoader("sample_policy.pdf")
docs = loader.load()

# -------------------------
# Embeddings
# -------------------------
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  # pass object directly

# -------------------------
# Create FAISS vectorstore
# -------------------------
vectorstore = FAISS.from_documents(docs, embeddings)  # pass embeddings object directly
retriever = vectorstore.as_retriever()

# -------------------------
# Build RetrievalQA chain with memory
# -------------------------
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    input_key="question",   # important for RAG Memory
    return_source_documents=False
)

# -------------------------
# Query function
# -------------------------
def multi_step_query(question: str) -> str:
    if not question or not question.strip():
        return "Please enter a question."
    
    # Pass question as dict to satisfy input_key
    return qa.run({"question": question})

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.1-8b-instant")

def summarize_documents(docs: list[Document]) -> str:
    chain = load_summarize_chain(llm, chain_type="map_reduce")
    return chain.run(docs)
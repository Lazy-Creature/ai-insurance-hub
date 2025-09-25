import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

memory = ConversationBufferMemory()
chat_model = ChatGroq(api_key=GROQ_API_KEY, model="llama-3.1-8b-instant")

conversation = ConversationChain(
    llm=chat_model,
    memory=memory
)

def ask_chatbot(question: str) -> str:
    return conversation.run(question)
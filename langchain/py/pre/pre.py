import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# env
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize a basic LLM
llm = OpenAI(temperature=0.7)

# Initialize a chat model
chat_model = ChatOpenAI()

# Basic LLM call
response = llm.predict("What is the capital of France?")
print(" . response:", response)

# Chat model interaction
from langchain.schema import HumanMessage
response = chat_model.predict_messages([
    HumanMessage(content="What is the capital of France?")
])
print(" . response:", response)

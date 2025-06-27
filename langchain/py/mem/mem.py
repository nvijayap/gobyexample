import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# env
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Initialize a basic LLM
llm = OpenAI(temperature=0.7)

# Conversation
conversation = ConversationChain(llm=llm, memory=ConversationBufferMemory())

# response1
response1 = conversation.predict(input="Hi, my name is Alice")
print(" . response1:", response1)

# response2 - The chain remembers "Alice"
response2 = conversation.predict(input="What's my name?")
print(" . response2:", response2)

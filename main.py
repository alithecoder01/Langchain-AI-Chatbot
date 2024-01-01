from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(temperature= 0.7)

name = llm("I have a dog, can you suggest 5 names for it ?")

print(name)
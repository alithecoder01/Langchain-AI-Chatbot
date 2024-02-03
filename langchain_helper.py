from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor

load_dotenv()

def genratename(animal_type, pet_color):
    llm = OpenAI(temperature= 0.7)

    promt_temp_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type}, it's {pet_color} in color. Can you suggest 5 names for it ?"
    )
    name_chain= LLMChain(llm= llm, prompt= promt_temp_name, output_key="pet_name")

    respons = name_chain({'animal_type': animal_type, 'pet_color': pet_color})

    return respons

def langchain_agent():
    llm = OpenAI(temperature = 0.7)

    tools = load_tools(["wikipedia", "llm-math"], llm=llm)

    # Get the prompt to use - you can modify this!
    prompt = hub.pull("hwchase17/react")

    # Create the ReAct agent
    agent= create_react_agent(llm,tools, prompt)
    
    # Create an agent executor by passing in the agent and tools, the verbose is to show the output
    resualt = AgentExecutor(agent=agent, tools=tools, verbose=True)

    # Add the prompt
    resualt.invoke({"input": "what is the bitcoin price now?"})


if __name__ == "__main__":
    langchain_agent()
    #print(genratename("cat","red"))
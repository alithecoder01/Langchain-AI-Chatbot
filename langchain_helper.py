from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentExecutor, create_react_agent
import numexpr
from langchain import hub

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
    llm = OpenAI(temperature= 0.7)

    #load tools 
    tools = load_tools(["wikipedia"], llm = llm)

    # Get the prompt to use - you can modify this!
    prompt = hub.pull("hwchase17/react")

    # Construct the ReAct agent
    agent = create_react_agent(llm, tools, prompt)

    # Create an agent executor by passing in the agent and tools, the verbose is to show the output
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    # Add the prompt
    agent_executor.invoke({"input": "what is the average age of a dog in 2023?"})
    

if __name__ == "__main__":
    langchain_agent()
    #print(genratename("cat","red"))
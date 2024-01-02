from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv


load_dotenv()

def genratename(animal_type, pet_color):
    llm = OpenAI(temperature= 0.7)

    promt_temp_name = PromptTemplate(
        input_variables=['animal_type', 'pet_color'],
        template="I have a {animal_type}, it's {pet_color} in color. Can you suggest 5 names for it ?"
    )
    name_chain= LLMChain(llm= llm, prompt= promt_temp_name)

    respons = name_chain({'animal_type': animal_type, 'pet_color': pet_color})

    return respons

if __name__ == "__main__":
    print(genratename("cat","red"))
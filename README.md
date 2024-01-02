from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key
llm = OpenAI(temperature=0.7)

def crickter(player):
    prompt_template_player=PromptTemplate(input_variables=["player"],
    template="What is the {player} nickname?")

    player_chain=LLMChain(llm=llm,prompt=prompt_template_player,output_key="city")

    #chain 2 city
    prompt_template_city=PromptTemplate(input_variables=["city"],
    template="which city he was born in{city}")
    
    city_chain=LLMChain(llm=llm,prompt=prompt_template_city,output_key="tourist")
    
    #sequentialchain
    chain=SequentialChain(chains=[player_chain,city_chain],
        input_variables=["player"],
        output_variables=["city","tourist"])
    
    response=chain({"player":player})
    return response
if __name__ == "__main__":
    print(crickter("Virat Kholi"))
   


















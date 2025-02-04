from dotenv import load_dotenv
import os
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

class Recipe_Selector:
    def __init__(self, pantry_data):
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        self.llm = ChatGoogleGenerativeAI(api_key=api_key, model="gemini-1.5-flash", temperature=0.3)
        self.pantry_data = pantry_data
        self.fresh_ingredients = pantry_data.loc[pantry_data["Category"] == "Fresh"]
        self.staples = pantry_data.loc[pantry_data["Category"] == "Staple"]
        prompt_template = PromptTemplate(
            input_variables=["fresh_ingredients", "staples"],
            template="""
                You are helping me plan out my meals based on what I have. I want to provide you
                a list of ingredients that I know for a fact that I have, and your job is to
                help me determine a main course that I can make using what I have. In addition, 
                a simple side dish to go with it is wanted if it is not a meal that would be 
                eaten without any. I want you to tell me 3 recipes that can be made for the main 
                course with what I tell you I have, and I will specify the one I want to get the 
                full instructions for.

                When selecting the recipes to make, try to ensure that they are different from
                each other as possible, since if I'm not in the mood for a certain style of food, 
                I still have a decent selection to choose from.

                These are ingredients I always keep on hand, and should be factored less: {staples}
                Fresh Ingredients: {fresh_ingredients}

                Answer:
            """
        )
        self.chain = LLMChain(llm=self.llm, prompt=prompt_template)

import sys
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit

from dotenv import load_dotenv
import os
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

class StoveWindow(QWidget):
    def __init__(self, main_window, pantry_window):
        super().__init__()
        self.main_window = main_window
        self.pantry_window = pantry_window
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stove/Oven")
        self.setGeometry(150, 150, 300, 200)
        
        layout = QVBoxLayout()
        
        self.suggest_button = QPushButton("Suggest Recipes!", self)
        self.suggest_button.clicked.connect(self.suggest_button_clicked)
        layout.addWidget(self.suggest_button)
        
        self.back_button = QPushButton("Back to Main Menu", self)
        self.back_button.clicked.connect(self.close_stove)
        layout.addWidget(self.back_button)
        
        self.recipe_label = QTextEdit(self)
        self.recipe_label.setReadOnly(True)
        layout.addWidget(self.recipe_label)

        self.setLayout(layout)
    
    def close_stove(self):
        self.main_window.show()
        self.close()

    def suggest_button_clicked(self):
        self.recipe_label.setText("PUSHED")
        load_dotenv()
        api_key = os.getenv("GEMINI_API_KEY")
        llm = ChatGoogleGenerativeAI(api_key=api_key, model="gemini-1.5-flash", temperature=0.3)

        pantry_data = self.pantry_window.get_pantry_data()  # Fetch latest pantry data
        
        # Convert DataFrames to lists of ingredients
        ingredients = pantry_data['Item Name'].tolist()
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
                I still have a decent selection to choose from. I want the answer formatted as:
                1. Recipe #1 Name
                2. Recipe #2 Name
                3. Recipe #3 Name

                These are main ingredients that I have: {ingredients}

                Answer:
            """
        )
        
        query = {
            "ingredients":ingredients,
        }
        self.chain = LLMChain(llm=llm, prompt=prompt_template)
        result = self.chain.invoke(query)["text"]

        print(result)
        self.recipe_label.setText(result)

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = StoveWindow(None)
    window.show()
    sys.exit(app.exec())

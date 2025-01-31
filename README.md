# Project_3

## Setting up the Environment:
### Packages
# TODO: Package settup instructions
## Requesting a Gemini API Key
(Copied from bookcamp spot)\
Before we get to building an AI-powered application, we will need to obtain an OpenAI API key.

1. Head over to the [Google developers website](https://ai.google.dev/gemini-api/docs/api-key) and register for a new account or log in to an existing one by first clicking the "Sign In" button in the top right of the page.

2. Once you're logged in you should be taken back to the developers page (or can use the link above to return there.) From that page, click "Get an API key".

3. You may be presented with the choices of using Google AI Studio or developing in your own environment. Choose to develop in your own environment by clicking "Get API key". Then read and respond to the legal notices and/or terms of service for the Gemini API.

4. You should be taken to the "API Keys" page. Click "Create API key" to generate an API key for developmental use. You will need to associate the API key with a development project. If you don't already have any projects to associate it with, choose "Create API key in new project.

5. After clicking creating the key you will be able to view and copy your key. This is the key we will use in our applications to make API calls to Gemini. You should be able to view the key again in the future if you need to, but it's still recommended that you record it somewhere securely for your own records.

6. Then, take the key that was generated and add it as a environmental varaible named GEMINI_API_KEY.

## Running
At it's most current state, please run the following commands in terminal
    pip install PySide6
Next navigate to to /project_3/scripts/ui using cd command
next run python kitchen_ui.py
This will launch the UI for the project.

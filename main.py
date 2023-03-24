# ## Simple Memory Chat Bot

# Welcome to the technical screen for the Machine Learning position! In this exercise, you will be tasked with building a chat bot that can run in a terminal. The chat bot should ask the user for input as to what persona it should act like, and it should have simple memory capabilities so that it can recall previous messages. You are free to use any programming language of your choice, but we recommend Python.

# ## **Requirements**

# 1. Create a chat bot that can run in a terminal.
# 2. The chat bot should ask the user for input as to what persona it should act like.
# 3. The chat bot should have simple memory capabilities so that it can recall previous messages.
# 4. Use any programming language of your choice, but we recommend Python.
# 5. Feel free to use a chat bot framework such as LangChain, Rasa, or ChatterBot to build your chat bot.

# ## **Evaluation Criteria**

# Your submission will be evaluated based on the following criteria:

# 1. **Functionality:** The chat bot should meet the requirements outlined above and function as expected.
# 2. **Code Quality:** The code should be well-structured, well-documented, and follow best practices.
# 3. **Memory Capabilities:** The chat bot should be able to remember previous messages and recall them when appropriate.
# 4. **Terminal Compatibility:** The chat bot should be able to run in a terminal.
# 5. **Bonus:** Dockerizing your solution is a major plus!!!

# ## **Submission**

# Please submit your solution as a GitHub repository or a ZIP file. Your submission should include:

# 1. All code and configuration files necessary to run the chat bot.
# 2. A README file with instructions on how to run the chat bot.
# 3. Any additional documentation or notes you would like to include.

from langchain.prompts import ( # for prompt templates
    ChatPromptTemplate, 
    MessagesPlaceholder, 
    SystemMessagePromptTemplate, 
    HumanMessagePromptTemplate
)
from langchain.chains import ConversationChain # for conversation chain
from langchain.chat_models import ChatOpenAI # for chat models
from langchain.memory import ConversationSummaryBufferMemory # for model memory
from dotenv import load_dotenv # for API key, env vars
import os # for API key, env vars
import json # for config

### get api key
load_dotenv()
key = os.environ.get('OPENAI_API_KEY')

### set app vars with config json
with open("config.json", "r") as f: app_vars = json.load(f)
model_name = app_vars["model_name"]
system_template = app_vars["system_template"]
input_prefix = app_vars["input_prefix"]
temperature = app_vars["temperature"]

### instantiate prompt from template
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    MessagesPlaceholder(variable_name="history"),
    HumanMessagePromptTemplate.from_template("{input}")
])

### instantiate llm
llm = ChatOpenAI(
	temperature=temperature,
	openai_api_key=key,
	model_name=model_name
)

### instantiate memory
memory = ConversationSummaryBufferMemory(llm=llm, return_messages=True)

### instantiate conversation chain
conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)

if __name__ == "__main__":
    print(f"\nModel Name: {model_name}")
    print(f"Temperature: {temperature}")
    print(f"System Template: '{system_template}'")
    print(f"Input Prefix: '{input_prefix}'\n")
    
    print("\n---Hit ^C or kill this Python process to exit.---\n")
    print("\n---Entering a chat with Ditto, your favorite shapeshifter! Be mindful, Ditto doesn't forget so easily.---\n")
    print("""\n   ⠀⠀⠀⢠⡜⠛⠛⠿⣤⠀⠀⣤⡼⠿⠿⢧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣀⡶⠎⠁⠀⠀⠀⠉⠶⠶⠉⠁⠀⠀⠈⠹⢆⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣀⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠶⠶⠶⠶⣆⡀⠀⠀⠀⠀
    ⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢣⡄⠀⠀⠀
    ⠛⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
    ⠀⠛⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠀⠀⠀⠀⢠⡼⠃⠀⠀
    ⠀⠀⠿⢇⡀⠀⠀⠀⠀⠀⠀⠀⠰⠶⠶⢆⣀⣀⣀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀
    ⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀
    ⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
    ⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢣⣤
    ⠀⣶⡏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿
    ⠀⠿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⢀⣀⣸⠿
    ⠀⠀⠙⢳⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡞⠛⠛⠛⠛⠛⠛⣶⣶⣶⣶⡞⠛⠃⠀\n""")
    
    first = True # flag, logic for deterministic first, non-first chat instances
    while True:
        if first: print("\nDitto: Hi trainer! I'm Ditto. I love to impersonate, and can easily morph into any persona you tell me. Go on, name a persona below:\n")
        elif not first: print("\nDitto: That was fun! Go on, name another persona:\n")
        first = False

        persona = input("Persona: ")
        inp = input_prefix + persona
        out = conversation.predict(input=inp)

        print("\nDitto: " + out)
        print("\n---Hit ^C or kill this Python process to exit.---\n")
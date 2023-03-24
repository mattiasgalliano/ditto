# ## Simple Memory Chat Bot

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
from dotenv import load_dotenv # for API key, env variables
import os # for API key, env variables
import json # for config

### get api key from either .env or passed env variable
load_dotenv()
key = os.environ.get('OPENAI_API_KEY')

### set config variables with config json
with open("config.json", "r") as f: config_vars = json.load(f)
model_name = config_vars["model_name"]
system_template = config_vars["system_template"]
input_prefix = config_vars["input_prefix"]
temperature = config_vars["temperature"]

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

### repeatedly solicit personas from user, generate associated model outputs all via CLI
def run():
    print(f"\nModel Name: {model_name}") # print config variables
    print(f"Temperature: {temperature}")
    print(f"System Template: '{system_template}'")
    print(f"Input Prefix: '{input_prefix}'\n")
    
    print("\n---Hit ^C or kill this Python process to exit.---\n") # exit info
    print("\n---Entering a chat with Ditto, your favorite shapeshifter! Be mindful, Ditto doesn't forget so easily.---\n") # intro
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
    print("\nDitto: Hi trainer! I'm Ditto. I love to impersonate, and can easily morph into any persona you tell me. Go on, name a persona below:\n")
    
    first = True # flag, logic for deterministic first, non-first persona solicitations
    while True:
        if not first: print("\nDitto: That was fun! Go on, name another persona:\n")
        first = False

        persona = input("Persona: ") # cli human input for persona 
        inp = input_prefix + persona # prepend prefix
        out = conversation.predict(input=inp) # run model inference, save output

        print("\nDitto: " + out) # print output
        print("\n---Hit ^C or kill this Python process to exit.---\n") # exit info

if __name__ == "__main__":
    run()
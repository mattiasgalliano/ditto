<h1>Ditto Chatbot</h1>

Ditto is an LLM-powered chatbot in your terminal that can emulate any persona. Have fun! :smile:

<h1>Requirements</h1>
Python 3.10 (https://www.python.org/downloads/release/python-3100/)<br \>
OpenAI API Key (https://platform.openai.com/account/api-keys)<br \>
Git (https://git-scm.com/) OR Docker (https://www.docker.com/)
<h1>Quickstart</h1>
Follow terminal commands below to start Ditto, replace XXX with your OpenAI API Key.
<h2>Setup</h2>

```
git clone https://github.com/mattiasgalliano/ditto.git
cd ditto
pip install -r "requirements.txt"
echo OPENAI_API_KEY="XXX" > .env
python -i main.py
```

<h2>With Docker</h2>

```
docker pull mattiasagalliano/ditto
docker run -ti -e OPENAI_API_KEY="XXX" mattiasagalliano/ditto
```

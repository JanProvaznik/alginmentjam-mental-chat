# Alignment Jam Prague 30.6-2.7.2023
- Jakub Stejskal, Jan Provaznik, Hana Kalivodova
## Steps

### Install deps: 

- `python3 -m pip install praw openai`

### Get Reddit questions:

- set Reddit credentials in `config.py`
- run `python3 reddit.py`

### Get ChatGPT answers:

- set OpenAI API key in `auth.py`
- Run `python chatgpt.py data/questions/<reddit-output-filename>`

### Get ChatGPT evaluations:

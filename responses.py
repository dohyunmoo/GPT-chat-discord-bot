import openai
import json

def handle_response(user_msg) -> str:

    with open('data.json') as f:
        data = json.load(f)

    openai.api_key = data['API-KEY']

    model = "text-davinci-003"
    response = openai.Completion.create(engine=model, prompt=user_msg, max_tokens=1024, n=1,stop=None,temperature=0.5)

    f.close()
    return '`' + str(response.choices[0].text[2:].strip('\n')) + '`'

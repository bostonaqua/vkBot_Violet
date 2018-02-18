from flask import Flask, request, json
from settings import token, confirmation_token
import messageHandler


app = Flask(__name__)


@app.route('/', methods=['POST'])
def processing():

    data = json.loads(request.data)
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    elif data['type'] == 'message_new':
        try:
            messageHandler.create_answer(data['object'], token)
        finally:
            return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

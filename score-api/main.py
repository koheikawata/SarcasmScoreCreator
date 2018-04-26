import os
from flask import Flask, request
from models.sarcasm import Sarcasm

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Sarcasm Score Creator!'

@app.route("/api/sarcasm/score", methods=['GET'])
def getScore():
    sentence = request.args.get('text')
    sarcasm = Sarcasm(sentence)
    
    return str(sarcasm.getScore())

if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', 'localhost')

    try:
      PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
      PORT = 5555

    app.run(HOST, PORT)

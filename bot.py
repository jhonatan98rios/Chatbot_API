#-*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
#import os
from flask import Flask, jsonify, request
from urllib.parse import unquote

app = Flask(__name__)

chats = [
    "Ola",
    "Tudo bem?",
    "Tudo sim e contigo?",
    "Tudo otimo",
    "Voce Programa?",
    "Sim, eu programo em python"
]

chatbot = ChatBot("Jonas")
#chatbot = ChatBot("Jonas", read_only=True)
trainer = ListTrainer(chatbot)
trainer.train(chats)

@app.route('/<string:talk>', methods=['GET']) # Recebe um argumento pela rota
def pesquisa(talk):

#   Struct
#   message = {
#      "author": "Jonas",
#      "message": "Hello World"
#   }
    
    resq = unquote(talk) # Converte em utf-8
    resp = chatbot.get_response(resq) # Gera a resposta
    response = {
        "author" : "Jonas",
        "message" : str(resp)
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)

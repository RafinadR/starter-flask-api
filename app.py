from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    a = "outrageous moth pants = епатажні штани від молі  (c)Google\n Roma Veles"
    return a

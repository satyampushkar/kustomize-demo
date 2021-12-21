from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Kustomization enthusiast!! from "+ os.environ.get('environment') +" environment!"
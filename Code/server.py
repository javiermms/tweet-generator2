from flask import Flask
# from stochastic_sampling import result

HTML = """<html><head><title>My App</title></head><body><h2>{}</h2></body></html>"""
app = Flask(__name__)

@app.route('/')
def hello_world():
    return HTML.format('Hello Darkness my old friend')
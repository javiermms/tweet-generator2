from flask import Flask
from Code.stochastic_sampling import probability
from Code.histogram_list import array

HTML = """<html><head><title>My App</title></head><body><h2>{}</h2></body></html>"""
app = Flask(__name__)

@app.route('/')
def hello_world():
    return HTML.format(probability(array))
from flask import Flask
from stochastic_sampling import probability
from histogram_list import array

HTML = """<html><head><title>My App</title></head><body><h2>{}</h2></body></html>"""
app = Flask(__name__)

@app.route('/')
def hello_world():
    words = []
    for _ in range(0, 8):
        words.append(probability(array))
    return ' '.join(words)

    # return HTML.format(str(a_list))
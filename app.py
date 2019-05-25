from flask import Flask
from markov_chain_second_order import create_markov, second_order_sentence
from clean_up_text import words_array

HTML = """<html><head><title>Tweet Generator</title></head><body><h2>{}</h2></body></html>"""
app = Flask(__name__)

@app.route('/')
def hello_world():
    return HTML.format(second_order_sentence(create_markov(words_array)))
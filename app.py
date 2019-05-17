from flask import Flask
# from stochastic_sampling import probability
# from histogram_list import array
from markov_chain_second_order import create_markov, second_order_sentence
from clean_up_text import words_array

HTML = """<html><head><title>My App</title></head><body><h2>{}</h2></body></html>"""
app = Flask(__name__)

@app.route('/')
def hello_world():
    # words = []
    # for _ in range(0, 8):
    #     words.append(probability(array))
    # return ' '.join(words)
    return second_order_sentence(create_markov(words_array))

    return HTML.format(str(a_list))
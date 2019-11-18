from flask import Flask
from markov_chain_second_order import create_markov, second_order_sentence
from clean_up_text import words_array

HTML = """<html><head><!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-150735145-1"></script>
</head><body><h2>{}</h2></body></html>"""
app = Flask(__name__)

@app.route('/')
def hello_world():
    return HTML.format(second_order_sentence(create_markov(words_array)))
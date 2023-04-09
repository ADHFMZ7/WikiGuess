from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():

    title = get_random_title()

    # Calls to get header, block of text
    block = get_block_

    
    length = len(block)



API_STRING = "For an article about %s, make a section titled %s that is %s characters long."




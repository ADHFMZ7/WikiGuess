from flask import Flask, render_template, request
import Wikipedia
from wiki import 

app = Flask(__name__)


correctButton = 'correct'
#create route for home page
@app.route('/')
def index():
    return render_template('index.html', right = Wikipedia.text, wrong =  )
#create route for clicked button
@app.route('/click', methods = ['POST'])
def click():
    clicked_button = request.form['clicked']
    if clicked_button == correctButton:
        render_template('win.html')
    else:
        render_template('lose.html')


def index():

    title = get_random_title()

    # Calls to get header, block of text
    block = get_block_

    
    length = len(block)



API_STRING = "For an article about %s, make a section titled %s that is %s characters long."



if __name__ == "__main__":
    app.run(debug = True)



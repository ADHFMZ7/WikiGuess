from flask import Flask, render_template, request
app = Flask(__name__)



#create route for home page
@app.route('/')
def index():
    return render_template('index.html')
#create route for guess
@app.route('/guess', methods = ['POST'])
def guess():
    guess_img = request.form['guess']
def index():

    title = get_random_title()

    # Calls to get header, block of text
    block = get_block_

    
    length = len(block)



API_STRING = "For an article about %s, make a section titled %s that is %s characters long."



if __name__ == "__main__":
    app.run(debug = True)



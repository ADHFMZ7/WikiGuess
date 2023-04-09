from flask import Flask, render_template, request
import wiki
import gpt

app = Flask(__name__)


correctButton = 'correct'
#create route for home page
@app.route('/')
def index():
    return render_template('index.html')
#create route for clicked button



# @app.route('/click', methods = ['POST'])
# def click():
#     clicked_button = request.form['clicked']
#     if clicked_button == correctButton:
#         render_template('win.html')
#     else:
#         render_template('lose.html')


@app.route('/game', )
def game():

    title = wiki.GetArticle()
    section = wiki.GetSection(title)
    subsection = wiki.GetSubsection(section)
    block = wiki.GetText(subsection) 
    length = wiki.GetLen(block)


    gpt.init_api("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")
    gen_text = gpt.gpt_api_call(title, subsection, length)
    
    

if __name__ == "__main__":
    app.run(debug = True)


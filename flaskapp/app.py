from flask import Flask, render_template, request, json
import wiki
import gpt

app = Flask(__name__)

#create route for home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/game')
def game():

    title = wiki.GetArticle()
    section = wiki.GetSection(title)
    subsection = wiki.GetSubsection(section)
    block = wiki.GetText(subsection) 
    length = wiki.GetLen(block)

    gpt.init_api("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")
    gen_text = gpt.gpt_api_call(title, subsection.title, length)

    data = {'title': title,
            'subsection': subsection.title,
            'wiki': block,
            'gpt': gen_text
            }

    return json.jsonify(data)

if __name__ == "__main__":
    app.run(debug = True)
    
        





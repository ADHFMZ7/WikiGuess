from random import randint
from flask import Flask, jsonify, render_template, request, json
import wiki
import gpt

articles = []

app = Flask(__name__)


def generate_articles():

    global articles

    for _ in range(10):

        title = wiki.GetArticle()
        section = wiki.GetSection(title)
        subsection = wiki.GetSubsection(section)
        block = wiki.GetText(subsection)
        length = wiki.GetLen(block)

        gen_text = gpt.gpt_api_call(title, subsection.title, length)
        
        num = randint(0, 1)

        data = {'title': title,
                'subsection': subsection.title,
                'wiki': block,
                'gpt': gen_text,
                'randNum' : num
                }

        articles.append(data)
    return articles


#create route for home page
@app.route('/')
def index():

    return render_template('index.html')


@app.route('/game')
def game():
    print("LEN OF ARTICLES", len(articles))
    if len(articles) <= 5:
        generate_articles()

    return jsonify(articles.pop())


    # THIS WILL SERVE A RANDOMLY SELECTED ARTICLE




if __name__ == "__main__":

    gpt.init_api("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")
    generate_articles()

    app.run(debug = True)





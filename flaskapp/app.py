from random import randint
from flask import Flask, jsonify, render_template, request, json
import wiki
import gpt

articles = []

app = Flask(__name__)
MAX_TOKENS = 1500

def generate_articles():

    global articles 

    if len(articles) > 5:
        return articles

    for _ in range(10):

        title = wiki.GetArticle()
        section = wiki.GetSection(title)
        subsection = wiki.GetSubsection(section)
        block = wiki.GetText(subsection)
        block = block if len(block) < MAX_TOKENS else block[:MAX_TOKENS]
        length = wiki.GetLen(block)

        # print(title)
        # print(section)
        # print(subsection)
        # print(block)
        # print(length)

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
    global articles 
    print("LEN OF ARTICLES", len(articles))
    if len(articles) <= 5:
        generate_articles()

    return jsonify(articles.pop())


    # THIS WILL SERVE A RANDOMLY SELECTED ARTICLE




if __name__ == "__main__":

    gpt.init_api("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")
    generate_articles()

    app.run(debug = False)





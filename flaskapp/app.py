from random import randint
from flask import Flask, jsonify, render_template, request, json
import wiki
import gpt
import start_articles

articles = start_articles.values
#articles = []

app = Flask(__name__)

def generate_articles():

    global articles 

    if len(articles) > 5:
        return articles

    for _ in range(15):

        title = wiki.GetArticle()
        section = wiki.GetSection(title)
        subsection = wiki.GetSubsection(section)
        block = wiki.GetText(subsection)
        length = wiki.GetLen(block)

        # print("\n\n")
        #
        # print(title)
        # print(subsection.title)
        # print(block)
        # print(length)

        gen_text = gpt.gpt_api_call(title, subsection.title, length)
       
        # print("GPT TEXT: ", gen_text)

        num = randint(0, 1)

        data = {'title': title,
                'subsection': subsection.title,
                'wiki': block,
                'gpt': gen_text,
                'randNum' : num
                }
        
        articles.append(data)

    print(articles)
    return articles 

def load_articles():
    pass

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
    #generate_articles()
    app.run(debug = False)

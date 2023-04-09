import requests
from bs4 import BeautifulSoup
import wikipediaapi
import random

articles = ["NATO"]
def GetArticle(artList=articles) ->str:
    return random.choice(artList)


def GetHeading(article=GetArticle()) -> str:
    #setting language English
    wiki = wikipediaapi.Wikipedia('en')

    #get page
    page = wiki.page(article)

    #create list of sections
    sections = []
    for section in page.sections:
        sections.append(section)
    return random.choice(sections)


def GetText(heading=GetHeading()) ->str:
    return heading.text


def GetLen(text: str) -> int:
    return len(text)

print(GetText())


    

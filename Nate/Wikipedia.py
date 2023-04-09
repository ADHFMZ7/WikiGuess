import requests
from bs4 import BeautifulSoup
import wikipediaapi
import random

# Define the parameters for the API request
params = {
   "action": "parse",
   "page": "Python_(programming_language)",
   "format": "json",
   "prop": "sections"
}


# Send the API request and retrieve the response as JSON
response = requests.get("https://en.wikipedia.org/w/api.php", params=params).json()


# Extract the section titles from the JSON response
sections = response["parse"]["sections"]


# Print the section titles
for section in sections:
   print(section["line"])



    

def GetHeading(article : str) -> str:
    #setting language English
    wiki = wikipediaapi.Wikipedia('en')

    #get page
    page = wiki.page(article)

    #create list of sections
    sections = []
    for section in page.sections:
        sections.append(section)
    return random.choice(sections)

def GetText(heading: str) ->str:
    return heading.text

def GetTextLength(text: str) -> int:
    return len(text)

    

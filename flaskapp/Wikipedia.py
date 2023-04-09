import wikipediaapi
import random

articles = ["NATO"]
def GetArticle(artList=articles) ->str:
    return random.choice(artList)

def GetLen(text: str) -> int:
    return len(text)

def GetText(subsection) ->str:
    return subsection.text

def GetSection(article=GetArticle()) -> str:
    #setting language English
    wiki = wikipediaapi.Wikipedia('en')

    #get page
    page = wiki.page(article)

    #create list of sections
    sections = []
    #adding wiki headings to sections
    for section in page.sections:
        sections.append(section)
    #choosing a subsection that is less than 3500 words
    valid = []
    for section in sections: #iterate through headings
        for subsection in section.sections: #iterate through subsections
            if GetLen(GetText(subsection)) <= 3500: #if the section has a subsection that is short, then add the section to valid
                valid.append(section)
    return random.choice(valid) #choose a valid section

def GetSectionName(section) -> str:
    return section.title

def GetSubsection(section: str) -> str:
    subsection = random.choice(section.sections)
    while len(GetText(subsection)) > 3500:
        subsection = random.choice(section.sections)
    return subsection

def GetSubsectionName(subsection: str) ->str:
    return subsection.title
article = GetArticle()
print("Article:", article)
heading = GetSection(article)
print("heading:", GetSectionName(heading))
subsection = GetSubsection(heading)
print("Subsection:", GetSubsectionName(subsection))
print("Text:")
text = GetText(subsection)


    
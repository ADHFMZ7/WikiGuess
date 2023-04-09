import wikipediaapi
import random
MAXLENGTH = 1500

titles = "Archaea – Bacteria – Bone Wars – Cooperative pulling paradigm – Cretaceous–Paleogene extinction event – DNA – DNA nanotechnology – Ediacaran biota – Evolution – Exosome complex – Fauna of Scotland – Fertilisation of Orchids – Flight feather – Flora of Madagascar – Genetics – History of biology – History of evolutionary thought – Immune system – Introduction to viruses – Lemurs of Madagascar (book) – Major urinary proteins – Metabolism – On the Origin of Species – Phagocyte – Preening – Proteasome – RNA interference – Rotating locomotion in living systems – Serpin – Toothcomb – Virus – Wells and Wellington affair"
titles = "Abraham Lincoln – Australia – Bible – Barack Obama – Canada – Charles III – China – Cleopatra – Cristiano Ronaldo – Darth Vader – Donald Trump – Dwayne Johnson – Elizabeth II – Elon Musk – Eminem – Facebook – Freddie Mercury – Game of Thrones – Germany – India – Johnny Depp – Japan – Justin Bieber – Kanye West – Kim Kardashian – Lady Gaga – LeBron James – Lionel Messi – Malware – Michael Jordan – Michael Jackson – Miley Cyrus – New York City – Russia – Search engine – Star Wars – Steve Jobs – Stephen Hawking – Taylor Swift – The Beatles – The Big Bang Theory – United Kingdom – United States Senate – World War I – World War II – YouTube"

titles = titles.split(" – ")

#articles = ["NATO"]
def GetArticle(artList=titles) ->str:
    return random.choice(artList)

def GetLen(text: str) -> int:
    return len(text)

def GetText(subsection) ->str:
    if len(subsection.text) > MAXLENGTH:
        return subsection.text[:MAXLENGTH]
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
        if section.title in ["Further reading", "Bibliography", "External links", "References", "See also"]:
            continue
        if len(GetText(section)) <= 10:
            continue
        #if section.sections:
        #    continue
        sections.append(section)
    #choosing a subsection that is less than 3500 words
    valid = []
    for section in sections: #iterate through headings
        for subsection in section.sections: #iterate through subsections
            if GetLen(GetText(subsection)) <= MAXLENGTH and GetLen(GetText(subsection)) >= 100: #if the section has a subsection that is short, then add the section to valid
                valid.append(section)
    if not valid:
        return random.choice(sections) #choose a valid section
    else:
        return random.choice(valid)

def GetSectionName(section) -> str:
    return section.title

def GetSubsection(section: str) -> str:
    if len(section.sections) == 0:
        return section
    subsection = random.choice(section.sections)
    while len(GetText(subsection)) > MAXLENGTH or len(GetText(subsection)) == 0:
        subsection = random.choice(section.sections)
    return subsection

def GetSubsectionName(subsection: str) ->str:
    return subsection.title

# article = GetArticle()
# print("Article:", article)
# heading = GetSection(article)
# print("heading:", GetSectionName(heading))
# subsection = GetSubsection(heading)
# print("Subsection:", GetSubsectionName(subsection))
# print("Text:")
# print(GetText(subsection))


    

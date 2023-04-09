from wikipediaapi import Wikipedia
import wikipediaapi
from gpt import init_api, gpt_api_call
import wiki

#init_api("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")

#output = gpt_api_call("NATO", "Bosnia and Herzegovina intervention", 3000)

#print(gpt_api_call("NATO", "Bosnia and Herzegovina intervention", 3000))

"""For an article about ", make a section titled "" that is about 0 characters long. The section is a part of a larger article about "Cretaceous–Paleogene extinction event".  Send only the section and omit the section's header. Write it in the style of an encyclopedia."""

titles = ["Cretaceous–Paleogene extinction event"]

b = wikipediaapi.Wikipedia("en")
article = wiki.GetArticle(titles)
for i in range(10):
    section = wiki.GetSection(article)
    subsection = wiki.GetSubsection(section)
    block = wiki.GetText(subsection)
    print(i)
    print(subsection.title, len(wiki.GetText(subsection)))
    #print(subsection.text)
    print("\n\n")

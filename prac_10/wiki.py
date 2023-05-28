"""
prompts the user for a page title or search phrase, then prints the summary of that page.
"""

import wikipedia

# response = wikipedia.search("Barack")
# print(response)

# response = wikipedia.suggest("Barak Obama")
# print(response)

# response = wikipedia.summary("Apple III", sentences=1)
# print(response)

title = input("A page title or search phrase: ")
while title != "":
    try: 
        summary = wikipedia.summary(title)
        page = wikipedia.page(title)
        print(f"Title: {page.title} ")
        print(f"URL: {page.url} ")
        print(summary)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    title = input("A page title or search phrase: ")

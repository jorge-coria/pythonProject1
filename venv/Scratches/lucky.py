# Opens several Google search results from text in clipboard

import requests, sys, webbrowser, bs4, pyperclip

print('Googling...')        # display text while downloading the Google page
res = requests.get('https://google.com/search?q=' + ''.join(pyperclip.paste()))
print('\'' + str(pyperclip.paste()) + '\'')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")

linkElems = soup.select('a:has(h3)')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    print(linkElems[i].get('href'))

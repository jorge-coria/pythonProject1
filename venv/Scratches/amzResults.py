# Opens several Amazon search results from text in clipboard
import requests, sys, webbrowser, bs4, pyperclip

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'referer': 'https://google.com',
}
print('Checking Amazon...')        # display text while downloading the Google page
res = requests.get('https://www.amazon.com/s?k=' + ''.join(pyperclip.paste()), headers=headers)
print('\'' + str(pyperclip.paste()) + '\'')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")

linkElems = soup.select('h2 a')

''' Print out every <a> tag
for i in range(len(linkElems)):
    print(linkElems[i])'''

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://amazon.com' + linkElems[i].get('href'))
    print(linkElems[i].get('href'))

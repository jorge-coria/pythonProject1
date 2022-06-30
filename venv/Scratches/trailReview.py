# Prints reviews for trail url that was in clipboard

import requests, sys, webbrowser, bs4, pyperclip

headers = {
    'User-Agent': 'Mozilla/5.0',
    'referer': 'https://google.com',
}

print('Getting Trail Page...')        # display text while downloading the Google page
res = requests.get(pyperclip.paste(), headers=headers)
print('\'' + str(pyperclip.paste()) + '\'')
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")

starRating = soup.select('.MuiRating-root default-module__rating___LhvGE MuiRating-sizeLarge MuiRating-readOnly')
print(starRating)
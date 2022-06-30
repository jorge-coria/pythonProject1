# Prints reviews for trail url that was in clipboard

from urllib.request import urlopen, Request
import requests, sys, webbrowser, bs4, pyperclip

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                        'AppleWebKit/537.11 (KHTML, like Gecko) '
                        'Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive',
            'Referer': 'https://www.google.com'}
request_obj = Request(pyperclip.paste(), headers = headers)
opened_url = urlopen(request_obj)
page_html = opened_url.read()
opened_url.close()
page_soup = soup(page_html, "html.parser")

#print('Getting Trail Page...')        # display text while downloading the Google page
#res = requests.get(pyperclip.paste(), headers=headers)
#print('\'' + str(pyperclip.paste()) + '\'')
#res.raise_for_status()

#soup = bs4.BeautifulSoup(res.text, features="html.parser")

starRating = page_soup.select('.MuiRating-root default-module__rating___LhvGE MuiRating-sizeLarge MuiRating-readOnly')
print(starRating)
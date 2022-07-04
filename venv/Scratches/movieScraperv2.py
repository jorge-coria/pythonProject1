# Scrapes the Rotten Tomatoes text reviews of a movie title read from user's clipboard

import bs4, pyperclip, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Open an incognito Chrome tab that stays open
o = webdriver.ChromeOptions()
o.add_argument('--incognito')
o.add_experimental_option('detach', True)
s = Service('C:/Users/Home/chromedriver.exe')
browser = webdriver.Chrome(service=s,options=o)
searchTerm = pyperclip.paste()
browser.get('https://www.rottentomatoes.com/search?search=' + ''.join(searchTerm))

# movieListElems is a list of movie titles returned as search results
WebDriverWait(browser, 20).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[slot]'))
)
movieListElems = browser.find_elements(By.CSS_SELECTOR, 'a[slot]')

# Iterate through search results for an exact match to our searchTerm and click it
for i in range(len(movieListElems)):
    if searchTerm == movieListElems[i].text:
        movieListElems[i].click()
        break

# reviewLink is a link to a full page of audience reviews, click it
WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'mop-audience-reviews__view-all--link'))
)
reviewLink = browser.find_element(By.CSS_SELECTOR, 'a[data-qa=audience-reviews-view-all-link]')
reviewLink.click()

time.sleep(5)

# Create a soup object and select the Review text on the current page
html = browser.page_source
soup = bs4.BeautifulSoup(html, features="html.parser")
reviewText = soup.select('p[data-qa=review-text]')

# Print out the list of audience reviews on the current page
for i in range(len(reviewText)):
    print('Review #' + str(i+1) + ': ' + str(reviewText[i].text))

# nextPageLink takes us to next page of movie reviews, click it
WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'prev-next-paging__button-text'))
)
nextPageLink = browser.find_element(By.CSS_SELECTOR, 'button[data-qa=next-btn]')
nextPageLink.click()

time.sleep(5)

# Create a soup object and select the Review text on the current page
html = browser.page_source
soup = bs4.BeautifulSoup(html, features="html.parser")
reviewText = soup.select('p[data-qa=review-text]')

# Print out the list of audience reviews on the current page
for i in range(len(reviewText)):
    print('Review #' + str(i+1) + ': ' + str(reviewText[i].text))

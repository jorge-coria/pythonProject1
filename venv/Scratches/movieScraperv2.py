# Scrapes the Rotten Tomatoes text reviews of a movie title read from user's clipboard

import bs4, pyperclip, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Create a soup object of current page and print out a list of the audience reviews
def get_page_review_soup():
    html = browser.page_source
    soup = bs4.BeautifulSoup(html, features="html.parser")
    page_review_text = soup.select('p[data-qa=review-text]')

    for i in range(len(page_review_text)):
        print('Review #' + str(i + 1) + ': ' + str(page_review_text[i].text))


# Clicks the next-page link to navigate to the next page of movie reviews
def click_next_page_link():
    next_page_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-qa=next-btn]'))
    )
    next_page_link.click()

    time.sleep(5)


# Open an incognito Chrome tab that stays open
o = webdriver.ChromeOptions()
o.add_argument('--incognito')
o.add_experimental_option('detach', True)
s = Service('C:/Users/Home/chromedriver.exe')
browser = webdriver.Chrome(service=s, options=o)
searchTerm = pyperclip.paste()
browser.get('https://www.rottentomatoes.com/search?search=' + ''.join(searchTerm))

# List of movie titles returned as search results
movie_title_list = WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[slot]'))
)

# Iterate through search results for an exact match to our searchTerm and click it
for i in range(len(movie_title_list)):
    if searchTerm == movie_title_list[i].text:
        movie_title_list[i].click()
        break

# Click link to navigate to the full page of audience reviews
reviewLink = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-qa=audience-reviews-view-all-link]'))
)
reviewLink.click()

time.sleep(5)

get_page_review_soup()

try:
    while True:
        click_next_page_link()
        get_page_review_soup()
except KeyboardInterrupt:
    exit(404)

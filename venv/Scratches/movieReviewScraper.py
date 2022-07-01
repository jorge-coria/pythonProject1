from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyperclip


s = Service('C:/Users/Home/chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('https://www.rottentomatoes.com/')

searchInputElem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'input'))
)
searchInputElem.send_keys(pyperclip.paste())
searchInputElem.send_keys(u'\ue007')

WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[slot]'))
)
movieListElems = browser.find_elements(By.CSS_SELECTOR, 'a[slot]')
for i in range(len(movieListElems)):
    print(movieListElems[i].text)

# TODO: Compare the list of text to search term, click the link of closest match

# TODO: Scrape Reviews from Movie WebPage


# buttonElem = browser.find_element(By.CSS_SELECTOR, 'button')
# buttonElem.click()

# passwordElem = browser.find_element_by_id('Passwd')
# passwordElem.send_keys('12345')
# passwordElem.submit()
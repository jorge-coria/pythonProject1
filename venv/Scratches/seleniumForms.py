from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


s = Service('C:/Users/Home/chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('http://gmail.com')

emailElem = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, 'input'))
)
emailElem.send_keys('not_my_real_email@gmail.com')

buttonElem = browser.find_element(By.CSS_SELECTOR, 'button')
buttonElem.click()

passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('12345')
passwordElem.submit()
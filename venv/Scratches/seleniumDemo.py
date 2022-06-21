from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


s = Service('C:/Users/Home/chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get('http://inventwithpython.com')

className = 'card-title'
elem = WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, className))
)

print("Found all elements' text with class name: %s :" % className)
for i in range(len(elem)):
    print("<%s>" % (elem[i].text))

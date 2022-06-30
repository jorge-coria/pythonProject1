# Prints reviews for trail url that was in clipboard

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pyperclip

s = Service('C:/Users/Home/chromedriver.exe')
browser = webdriver.Chrome(service=s)
browser.get(pyperclip.paste())

reviewText = browser.find_element(By.XPATH, "//p[@itemprop='reviewBody']")

print(reviewText)

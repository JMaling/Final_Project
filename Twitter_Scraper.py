from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = "https://twitter.com/search?q=" + "celebrityname" + "&src=tyah&lang=en"
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)

htmlSource = driver.page_source
soup = BeautifulSoup(htmlSource, "html.parser")
tweets = soup.findAll("p", class_="tweet-text")

words = [x.text.split() for x in tweets]

just_words = []
for word in words:
    just_words += word
print(just_words)
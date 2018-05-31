from bs4 import BeautifulSoup
from selenium import webdriver
import time

def twitter_scraper(string):
    name_list = string.split()
    url = "https://twitter.com/search?q="
    for i in range(len(name_list)):
        if i < len(name_list) - 1:
            url += name_list[i] + "%20"
        else:
            url += name_list[i]
    url += "&src=tyah&lang=en"
    print(url)
    print(name_list)

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    for i in range(4):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)

    htmlSource = driver.page_source
    soup = BeautifulSoup(htmlSource, "html.parser")
    tweets = soup.findAll("p", class_="tweet-text")

    words = [x.text.split() for x in tweets]
    
    just_words = []
    for word in words:
        just_words += word
    word_list1 = [word.strip() for word in just_words if ".com" not in word]
    word_list2 = [word for word in word_list1 if "#" not in word]
    word_list3 = [word for word in word_list2 if "http" not in word]
    word_list4 = [word for word in word_list3 if "@" not in word]
    word_list5 = [word for word in word_list4 if "." not in word]
    word_list6 = [word for word in word_list5 if "-" not in word]
    return word_list6
if __name__ == "__main__":
    twitter_scraper("wrvdsd")
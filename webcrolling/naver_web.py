import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

try:
    new_title_get = []
    next_page = []

    browser = webdriver.Chrome()
    browser.get("https://www.naver.com/")
    time.sleep(1)
    browser.find_element(By.CLASS_NAME, "search_input").send_keys("it회사")
    browser.find_element(By.CLASS_NAME, "search_input").send_keys(Keys.ENTER)
    time.sleep(1)
    browser.find_element(By.LINK_TEXT, "뉴스").send_keys(Keys.ENTER)
    #browser.find_element(By.XPATH, '//*[@id="snb"]/div[1]/div/div[1]/a[2]').click()

    newstable = browser.find_elements(By.CLASS_NAME, "news_tit")
    for j in range(999):
        try:
            time.sleep(2)
            for i in range(len(newstable)):
                newstable = browser.find_elements(By.CLASS_NAME, "news_tit")
                news_rink = newstable[i].get_attribute("href")
                news_ti = newstable[i].get_attribute("innerText")
                new_title_get.append([news_ti, news_rink])
            browser.find_element(By.CLASS_NAME, "btn_next").click()
        except:
            break

    browser.close()
except Exception as i:
    print(i)

with open("news.csv", 'w', encoding="utf-8-sig", newline="") as file:
    write = csv.writer(file)
    write.writerows(new_title_get)

import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import clipboard
from selenium.webdriver.common.action_chains import ActionChains

a = []
b=[]
browser = webdriver.Chrome()
browser.get("https://www.foodsafetykorea.go.kr/portal/healthyfoodlife/searchHomeHF.do?menu_grp=MENU_NEW01&menu_no=2823#")
time.sleep(2)
click_ti = browser.find_element(By.XPATH, ('//*[@id="search_word"]'))
click_ti.send_keys("다이어트")
time.sleep(1)
click_ti.send_keys(Keys.ENTER)
time.sleep(1)
browser.find_element(By.ID, "show_cnt").click()
time.sleep(1)
browser.find_element(By.XPATH, '//*[@id="show_cnt"]/option[3]').click()
time.sleep(1)
browser.find_element(By.ID, "show_cnt-btn").click()
time.sleep(1)
for i in range(0, len(browser.find_elements(By.CLASS_NAME, 'table_txt'))):
    if i%5 == 1:
        a.append(browser.find_elements(By.CLASS_NAME, 'table_txt')[i].get_attribute("innerText"))
    elif i%5 == 2:
        a.append(browser.find_elements(By.CLASS_NAME, 'table_txt')[i].get_attribute("innerText"))
        browser.find_elements(By.CLASS_NAME, 'table_txt')[i].click()
        time.sleep(1)
        a.append(browser.find_element(By.ID, 'copyUrl').get_attribute("value"))
        browser.back()
        time.sleep(1)
        b.append(a)
        a=[]

df = pd.DataFrame(b, columns=["제품명", "업소명", "URL"])
js = df.to_json(orient="records")
with open('다이어트 데이터.json', 'w', encoding="utf-8-sig") as f:
    f.write(js)
browser.quit()
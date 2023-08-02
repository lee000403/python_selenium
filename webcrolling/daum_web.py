import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sqlalchemy
import pymysql
import csv

# browser = webdriver.Chrome()
# browser.get('https://finance.daum.net/domestic/market_cap')

# while browser.find_elements(By.CLASS_NAME, 'btnNext'):
#     for i in range(0, len(browser.find_elements(By.CLASS_NAME, 'btnMove'))):
#         df = pd.read_html(browser.page_source)[1]
#         df.dropna(axis='index', how='all', inplace=True)
#         df.dropna(axis='columns', how='all', inplace=True)

#         button_next = browser.find_elements(By.CLASS_NAME, 'btnMove')[i]
#         button_next.click()
#         time.sleep(1)
#     browser.find_element(By.CLASS_NAME, 'btnNext').click()
#     time.sleep(1)

conn = pymysql.connect(host="localhost", user="root", password="!yojulab*", db="db_cars", charset="utf8")
cur = conn.cursor()

f = open('다음_주식.csv', encoding="utf-8-sig")
rdr = csv.reader(f)
list_data = []

for i in list(rdr)[1:20]:
    i = i[0:3]
    list_data.append(i)

sql = """insert into news (id, news_title, news_url) values (%s, %s, %s)"""
cur.execute(sql, *list_data)
conn.commit()

conn.close()
# browser.quit()
    
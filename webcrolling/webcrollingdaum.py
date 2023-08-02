import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://finance.daum.net/'
browser.get(url)

button_korea = browser.find_element(By.XPATH, '//a[@href="/domestic"]')
button_korea.click()

button_siga = browser.find_element(By.XPATH, '//a[@href="/domestic/market_cap"]')
button_siga.click()

for idx in range(1, 10):        
    df= pd.read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True)
    df.dropna(axis='columns', how='all', inplace=True)

    f_name = '다음_주식1.csv'
    if os.path.exists(f_name):
        df.to_csv(f_name, encoding='utf-8-sig',index=False , mode='a', header=False)
    else:
        df.to_csv(f_name, encoding="utf-8-sig", index=False)
    
    button_next2 = browser.find_elements(By.CLASS_NAME, 'btnMove')
    button_next2.click()

browser.quit()



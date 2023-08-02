import os 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://finance.naver.com/sise/sise_market_sum.naver?&page='
browser.get(url)

checkboxes = browser.find_elements(By.NAME, 'fieldIds')
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

item_list = ["부채총계", " PER", "고가", "저가"]
for checkbox in checkboxes:
    parent = checkbox.find_element(By.XPATH, '..')
    lable = parent.find_element(By.TAG_NAME, 'label')
    if lable.text in item_list:
        checkbox.click()

btn_apply = browser.find_element(By.XPATH, '//a[@href="javascript:fieldSubmit()"]')
btn_apply.click()

for idx in range(1, 11):
    browser.get(url + str(idx))

    df = pd.read_html(browser.page_source)[1]
    df.dropna(axis='index', how='all', inplace=True)
    df.dropna(axis='columns', how='all', inplace=True)
    if len(df) == 0:
        break

    f_name = '사자.csv'
    if os.path.exists(f_name):
        df.to_csv(f_name, encoding='utf-8-sig', index=False, mode='a', header=False)
    else:
        df.to_csv(f_name, encoding='utf-8-sig', index=False)

browser.quit()

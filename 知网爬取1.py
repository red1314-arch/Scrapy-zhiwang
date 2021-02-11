from selenium import webdriver
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import time


list_href = []
list_title = []
list_time = []
list_keyword = []

url = 'https://kns.cnki.net/kns/brief/result.aspx?dbprefix=scdb'
driver = webdriver.Firefox()
driver.get(url)

#input = driver.find_elements_by_xpath('//*[@id="txt_2_logical"]')

select_1 = Select(driver.find_element_by_xpath('//*[@id="txt_2_logical"]'))

select_1.select_by_visible_text("或者")

select_1 = Select(driver.find_element_by_xpath('//*[@id="txt_2_sel"]'))

select_1.select_by_visible_text("主题")


input_1 = driver.find_element_by_xpath('//*[@id="txt_1_value1"]')
input_1.send_keys('大学生总体国家安全观')

input_2 = driver.find_element_by_xpath('//*[@id="txt_2_value1"]')
input_2.send_keys('大学生国家安全教育')

jiansuo = driver.find_element_by_xpath('//*[@id="btnSearch"]')
jiansuo.click()

time.sleep(5)

driver.switch_to.frame('iframeResult')
for i in range(1,12):


    element_href = driver.find_elements_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[2]/a')
    for item in element_href:
        list_href.append('https://kns.cnki.net/'+item.get_attribute('href')[21:].replace('kns','KCMS'))

    for item in element_href:
        list_title.append(item.text)

    element_time = driver.find_elements_by_xpath('/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td[5]')
    for item in element_time:
        list_time.append(item.text)


    #driver.find_element_by_xpath('/html/body/form/table/tbody/tr[3]/td/table/tbody/tr/td/div/a[9]').click()
    driver.find_element_by_xpath('//*[@id="Page_next"]').click()
    time.sleep(5)


print(list_href,len(list_href))
print(list_title,len(list_title))
print(list_time,len(list_time))

for url in list_href:
    driver.get(url)
    keyword = driver.find_elements_by_class_name('keywords')
    time.sleep(2)
    for item in keyword:
        list_keyword.append(item.text)


print(list_keyword,len(list_keyword))

data_1 = {
    'title':list_title
}

data_2 = {
    'time':list_time
}

data_3 = {
    'keyword':list_keyword
}

data_1 = pd.DataFrame(data_1)
data_1.to_excel('title.xlsx')

data_2 = pd.DataFrame(data_2)
data_2.to_excel('time.xlsx')

data_3 = pd.DataFrame(data_3)
data_3.to_excel('keyword.xlsx')




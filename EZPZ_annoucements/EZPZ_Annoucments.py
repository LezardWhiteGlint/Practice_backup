#!/usr/bin/env python
from selenium import webdriver
import os
import time
import io
driver = webdriver.Chrome(executable_path='/Users/lezardvaleth/Documents/Python/chromedriver')
os.chdir('/Users/lezardvaleth/Documents/Python/EZPZ_annoucements')

#login in backend
def login():
    driver.get('http://54.173.233.19/announcement/www/index.php/announcement/www/index.php')
    account = driver.find_element_by_id('username')
    password = driver.find_element_by_id('password')
    login = driver.find_elements_by_xpath('//*[@id="login-box"]/div/div/form/fieldset/div[2]/button')
    account.send_keys('guest')
    password.send_keys('123456')
    login[0].click()

#Navigate to the input page
def navi(lang):
    driver.get('http://54.173.233.19/announcement/www/index.php/announcement/www/index.php?mod=Announce&do=add')
    area = driver.find_element_by_xpath('//*[@id="selectArea"]/option[2]')
    area.click()
    time.sleep(1)
    lang = driver.find_element_by_xpath('//*[@id="selectLang"]/option['+str(lang)+']')
    lang.click()

#input content
def inputcontent(language):
    driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="econtent"]'))
    content = driver.find_element_by_xpath('/html/body')
    for line in language:
        content.send_keys(line)
    driver.switch_to.default_content()
    submit = driver.find_element_by_xpath('//*[@id="main-container"]/div/div[2]/div[2]/div/div/div/div[2]/div/form/div[3]/button')
    submit.click()
    time.sleep(2)
    alert = driver.switch_to_alert()
    alert.accept()


#get annoucement content
annoucement = []
f = io.open('test.txt','r',encoding='utf-16-le')
for line in f:
    annoucement.append(line)

#slice the annoucement content into different language
English = []
French = []
German = []
Spanish = []
Portu = []
Russian = []
Thai = []

EnglishIndex = 1
FrenchIndex = annoucement.index('French\n')
GermanIndex = annoucement.index('German\n')
SpanishIndex = annoucement.index('Spanish\n')
PortuIndex = annoucement.index('Portu\n')
RussianIndex = annoucement.index('Russian\n')
ThaiIndex = annoucement.index('Thai\n')

for ele in annoucement[EnglishIndex:]:
    if ele == 'French\n':
        break
    English.append(ele)

for ele in annoucement[FrenchIndex+1:GermanIndex]:
    if ele == 'German\n':
        break
    French.append(ele)

for ele in annoucement[GermanIndex+1:SpanishIndex]:
    if ele == 'Spanish\n':
        break
    German.append(ele)

for ele in annoucement[SpanishIndex+1:PortuIndex]:
    if ele == 'Portu\n':
        break
    Spanish.append(ele)

for ele in annoucement[PortuIndex+1:RussianIndex]:
    if ele == 'Russian\n':
        break
    Portu.append(ele)

for ele in annoucement[RussianIndex+1:ThaiIndex]:
    if ele == 'Thai\n':
        break
    Russian.append(ele)

for ele in annoucement[ThaiIndex+1:]:
    Thai.append(ele)





login()
navi(2) #english
inputcontent(English)
navi(3) #french
inputcontent(French)
navi(4) #German
inputcontent(German)
navi(5) #Spanish
inputcontent(Spanish)
navi(6) #Portu
inputcontent(Portu)
navi(8) #Russian
inputcontent(Russian)
navi(10) #Thai
inputcontent(Thai)



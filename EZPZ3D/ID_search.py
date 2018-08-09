from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import openpyxl
import os
import time
driver = webdriver.Chrome(executable_path='/Users/lezardvaleth/Documents/Python/chromedriver')
os.chdir('/Users/lezardvaleth/Documents/Python/EZPZ3D')

#login in backend
def login():
    driver.get('http://34.237.161.188/portal')
    account = driver.find_element_by_xpath('/html/body/div[2]/form/div[2]/div/div/input')
    password = driver.find_element_by_xpath('/html/body/div[2]/form/div[3]/div/div/input')
    login = driver.find_elements_by_xpath('/html/body/div[2]/form/div[4]/button')
    account.send_keys('admin')
    password.send_keys('000000')
    login[0].click()

#navigate to the page
def query(district,char_name):
    driver.get('http://34.237.161.188/portal/query-account?platform=2&district='+str(district))
    character = driver.find_element_by_xpath('//*[@id="heroName"]')
    query = driver.find_element_by_xpath('//*[@id="validateForm"]/div/div[12]/button[1]')
    character.send_keys(char_name)
    query.click()
    time.sleep(1)
    uid = driver.find_element_by_xpath('//*[@id="heroUUID"]')
    result = uid.get_attribute('value')
    return result

#get district and char name
def excution():
    temp = openpyxl.load_workbook('id.xlsx')
    sheet = temp.get_sheet_by_name('Sheet1')
    result = []
    i = 1
    while True:
        i += 1
        if sheet['A'+str(i)].value == None:
            break
        district = sheet['A'+str(i)].value
        char_name = sheet['B'+str(i)].value
        result.append(query(district,char_name))
    for r in result:
        print(r)
        
    

login()
excution()
driver.quit()






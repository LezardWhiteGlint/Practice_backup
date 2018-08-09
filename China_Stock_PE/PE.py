from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1800x1600')
import openpyxl
import os
import time
driver = webdriver.Chrome(executable_path='/Users/lezardvaleth/Documents/Python/chromedriver',chrome_options=options)
os.chdir('/Users/lezardvaleth/Documents/Python/China_Stock_PE')

#go to page
def login():
    url = 'http://www.sse.com.cn/market/stockdata/overview/day/'
    driver.get(url)

#navi back to the starting point
def initialize(click_times):
    driver.execute_script("window.scrollTo(0, 200)")
    panel = driver.find_element_by_xpath('//*[@id="start_date2"]')
    previous = driver.find_element_by_xpath('/html/body/div[14]/div[3]/table/thead/tr[1]/th[1]/i')
    panel.click()
    for i in range(click_times):
        previous.click()

#get current date
def current_date():
    date = driver.find_element_by_xpath('//*[@id="start_date2"]')
    current_date = date.get_attribute('value')
    return current_date

#check if the date is the first day of the month, if so return true
def first_day_every_month():
    day = current_date().split('-')[2]
    if day == '01':
        return True
    return False

#the date to stop iteration        
#def stop_date(date):
#    if current_date() == date:
#        return True
#    return False


#select date
def date_selector(row, column):
    panel = driver.find_element_by_xpath('//*[@id="start_date2"]')
    date_select = driver.find_element_by_xpath('/html/body/div[14]/div[3]/table/tbody/tr['+str(row)+']/td['+str(column)+']')
    check_button = driver.find_element_by_xpath('//*[@id="btnQuery"]')
    date_select.click()
    check_button.click()
    panel.click()

#log the data
def log():
    result = 0
    i = 0
#    element = WebDriverWait(driver,10).until(
#        EC.presence_of_element_located((By.XPATH, '//*[@id="tableData_934"]/div[2]/table/tbody/tr[7]/td[2]/div')))
#    time.sleep(0.01)
    try:
        result_temp = driver.find_element_by_xpath('//*[@id="tableData_934"]/div[2]/table/tbody/tr[7]/td[2]/div')
        result = float(result_temp.text)
    except NoSuchElementException:
        pass
    except StaleElementReferenceException:
        pass
    return result

#iterate through the page, output result
def iteration(count_down,row):
    result = {}
    while row<7:
        for c in column:
            if count_down == 0:
                break
#            element = WebDriverWait(driver,10).until(
#                EC.presence_of_element_located((By.XPATH, '//*[@id="tableData_934"]/div[2]/table/tbody/tr[7]/td[2]/div')))
            date_selector(row,c)
            result[current_date()] = log()
            if first_day_every_month():
                row = 2
            count_down -= 1
#            print(count_down)
        row += 1
    return result

#record the result in excel
def excel(result,excel_start_row):
    file = openpyxl.load_workbook('PE.xlsx')
    sheet = file.get_sheet_by_name('Sheet1')
    for i in result:
        sheet['A'+str(excel_start_row)]=i
        sheet['B'+str(excel_start_row)]=result[i]
        excel_start_row +=1
    file.save('PE.xlsx')

def app():
    login()
    time.sleep(3)
    initialize(go_back_months)
    result = iteration(count_down,row)
    excel(result,excel_start_row)
    
    

    
result = {}
row = 2
column = [1,2,3,4,5,6,7]
go_back_months = 216
count_down = 1800
excel_start_row = 3790
app()


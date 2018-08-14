from Web_scrapper import normal_mode
from Web_scrapper import headless_mode
from datetime import date,timedelta
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient
import pymongo


#go to page
def login(driver):
    url = 'http://www.sse.com.cn/market/stockdata/overview/day/'
    driver.get(url)
    driver.execute_script("window.scrollTo(0, 200)")


#navi back to the starting point
def initialize(start_date,driver):
    panel = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="start_date2"]')))
    #panel = driver.find_element_by_xpath('//*[@id="start_date2"]')
    previous = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[14]/div[3]/table/thead/tr[1]/th[1]/i')))
    #previous = driver.find_element_by_xpath('/html/body/div[14]/div[3]/table/thead/tr[1]/th[1]/i')
    panel.click()
    previous.click()
    #for i in range(click_times):
    #    previous.click()
    r = 1
    c = 1
    for i in range(14):
        date = driver.find_element_by_xpath('/html/body/div[14]/div[3]/table/tbody/tr['+str(r)+']/td['+str(c)+']')
        if date.text == '1':
            date.click()
            break
        if c == 7:
            r = 2
            c = 1
        else:
            c +=1
    panel = driver.find_element_by_xpath('//*[@id="start_date2"]')
    if panel.get_attribute('value') == str(start_date):
        pass
    else:
        initialize(start_date,driver)            

def next_day(current_date,driver):
    try:
        nextday = current_date + timedelta(days=1)
        panel = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="start_date2"]')))
        panel.click()
        if nextday.day < current_date.day:
            nextmonth = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[14]/div[3]/table/thead/tr[1]/th[3]/i')))
            nextmonth.click()
        r = 1
        c = 1
        for i in range(42):
            date = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[14]/div[3]/table/tbody/tr['+str(r)+']/td['+str(c)+']')))
            #if int(date.text) == 1 and r > 3 :
             #   date.click()
            panel = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="start_date2"]')))
            if r < 3 and int(date.text) > 20:
                backward_prevent = False
            else:
                backward_prevent = True
            if date.text == str(nextday.day) and backward_prevent:
                date.click()
                break
            if c == 7:
                r += 1
                c = 1
            else:
                c +=1
        return nextday
    except StaleElementReferenceException:
        print('StaleElementReferenceException from next_day function')
        return nextday
        pass
        
    
 

def info_getter(Collection,driver,query_date):
    try:
        if query_date.isoweekday() <= 5:
            total_stock_value = WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tableData_934"]/div[2]/table/tbody/tr[2]/td[2]/div')))
            trading_value = WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tableData_934"]/div[2]/table/tbody/tr[3]/td[2]/div')))
            traded_volum = WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tableData_934"]/div[2]/table/tbody/tr[4]/td[2]/div')))
            traded_amount = WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tableData_934"]/div[2]/table/tbody/tr[5]/td[2]/div')))
            traded_times = WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tableData_934"]/div[2]/table/tbody/tr[6]/td[2]/div')))
            average_PE = WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tableData_934"]/div[2]/table/tbody/tr[7]/td[2]/div')))
            exchange_rate = WebDriverWait(driver,3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tableData_934"]/div[2]/table/tbody/tr[8]/td[2]/div')))
            post = { 'total_stock_value(100M_RMB)' : float(total_stock_value.text),
                    'trading_value(100M_RMB)' : float(trading_value.text),
                    'trade_volum(10K_Unit)' : float(traded_volum.text),
                    'trade_amount(100M_RMB)' : float(traded_amount.text),
                    'traded_times(10K_times)' : float(traded_times.text),
                    'average_PE' : float(average_PE.text),
                    'exchange_rate' : float(exchange_rate.text),
                    'date': str(query_date) }
            Collection.insert_one(post)
            print(str(query_date)+' data inserted')
    except NoSuchElementException:
        print('NoSuchElementException from info_getter function')
        pass
    except TimeoutException:
        print('TimeoutException from info_getter function')
        pass
    except StaleElementReferenceException:
        print('StaleElementReferenceException from info_getter function')
        pass
    except ValueError:
        print('Value Error from info_getter function')
        pass

    
def main():    
    '''change parameters in main function'''
    client = MongoClient()
    DB = client.China_stock
    Collection = DB.Shanghai_stock
    Collection.create_index([('date',pymongo.ASCENDING)],unique = True)
    start_date = date(2000,1,1)

    driver = headless_mode()
    #driver = normal_mode()
    login(driver)
    print('Going back to start date')
    initialize(start_date,driver)
    current_date = start_date
    while True:
        query_button = driver.find_element_by_xpath('//*[@id="btnQuery"]')
        query_button.click()
        time.sleep(0.1)
        info_getter(Collection,driver,current_date)
        current_date = next_day(current_date,driver)
        if current_date == date(2018,8,10):
            break
    

if __name__ == "__main__":
    main()

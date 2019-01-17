from Web_scrapper import login
from Web_scrapper import normal_mode
from Web_scrapper import headless_mode
from datetime import date,timedelta
import time
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient


#a function iterate through the page and put the revenue info in the data base
def info_getter(driver,date):
    client = MongoClient()
    DB = client.Mobile_revenue
    Collection = DB.revenue
    i = 2
    while True:
        try:
            rank = driver.find_element_by_xpath('//*[@id="__t_grid_0"]/tbody/tr['+str(i)+']/td[1]')
            game = driver.find_element_by_xpath('//*[@id="__t_grid_0"]/tbody/tr['+str(i)+']/td[2]')
            revenue = driver.find_element_by_xpath('//*[@id="__t_grid_0"]/tbody/tr['+str(i)+']/td[3]')
            paid_player = driver.find_element_by_xpath('//*[@id="__t_grid_0"]/tbody/tr['+str(i)+']/td[4]')
            paid_count = driver.find_element_by_xpath('//*[@id="__t_grid_0"]/tbody/tr['+str(i)+']/td[5]')
            arppu = driver.find_element_by_xpath('//*[@id="__t_grid_0"]/tbody/tr['+str(i)+']/td[6]')
            post = { 'rank' : int(rank.text),
                     'game' : game.text,
                     'revenue' : float(revenue.text),
                     'paid_player' : int(paid_player.text),
                     'paid_count' : int(paid_count.text),
                     'arppu' : float(arppu.text),
                     'date' : date.isoformat() }
            Collection.insert_one(post)
            print(str(date)+' data inserted')
            i += 1
        except NoSuchElementException:
            break
        
#a function to navigate through pages and put info into data base
def page_navi(driver,sleep_time,start_date,end_date):
    time.sleep(sleep_time)
    date = start_date
    while True:
        url = 'http://data.r2games.com/mobile/?r=complex%2Frank&m=M356&p=mobile&time='+ date.isoformat()
        driver.get(url)
        info_getter(driver,date)
        if date == end_date:
            break
        else:
            date = date + timedelta(days=1)
    
def main():
    #set parameters
    sleep_time = 0.5
    start_date = date(2018,10,17)
    end_date = date(2018,10,28)

    #login and initiate
    url = 'http://acc.r2games.com/main/?r=site/login'
    account_xpath = '//*[@id="login-form"]/dl/dd[1]/input'
    password_xpath = '//*[@id="login-form"]/dl/dd[2]/input'
    login_xpath = '//*[@id="submit-btn"]'
    account_content = '10024'
    password_content = 'yyy666'
    driver = headless_mode()
    login(driver,url,account_xpath,password_xpath,login_xpath,account_content,password_content)
    #navigate and get info
    page_navi(driver,sleep_time,start_date,end_date)
    driver.quit()

if __name__ == "__main__":
    main()


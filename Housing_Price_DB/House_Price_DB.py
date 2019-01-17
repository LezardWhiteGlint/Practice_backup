from Web_scrapper import normal_mode
from datetime import date,timedelta
import time
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient

# return next month date object
def next_month(start_date):
    nextmonth = start_date
    while True:
        if int(nextmonth.year) > int(start_date.year):
            break
        if int(nextmonth.month) > int(start_date.month):
            break
        else:
            nextmonth = nextmonth + timedelta(days=1)
    return nextmonth


# get info and put into database
def info_getter(Collection,driver,query_date,city_level):
    i = 1
    while True:
        try:
            city = driver.find_element_by_xpath('//*[@id="order_f"]/tr['+str(i)+']/td[2]/a')
            price = driver.find_element_by_xpath('//*[@id="order_f"]/tr['+str(i)+']/td[3]')
            MoM = driver.find_element_by_xpath('//*[@id="order_f"]/tr['+str(i)+']/td[4]')
            YoY = driver.find_element_by_xpath('//*[@id="order_f"]/tr['+str(i)+']/td[5]')
            if price.text == '--' or price.text == '':
                price_value = None
            else:
                price_value = int(price.text.replace(',',''))
            if MoM.text == '--' or MoM.text == '':
                MoM_value = None
            else:
                MoM_value = float(MoM.text.strip('%'))/100
            if YoY.text == '--' or YoY.text == '':
                YoY_value = None
            else:    
                YoY_value = float(YoY.text.strip('%'))/100
            post = { 'city' : city.text,
                     'city_level' : city_level,
                     'price' : price_value,
                     'MoM' : MoM_value,
                     'YoY' : YoY_value,
                     'date': str(query_date) }
            if price_value != None:
                Collection.insert_one(post)
            i += 1
            if i == 21:
                break
        except NoSuchElementException:
            break

def page_navi(Collection,city_level,driver,sleep_time,start_date,end_date):
    time.sleep(sleep_time)
    date = start_date
    while True:
        url = 'http://www.creprice.cn/rank/cityforsale.html?type=11&y='+str(date.year)+'&m='+str(date.month)+'&citylevel='+str(city_level)
        driver.get(url)
        info_getter(Collection,driver,date,city_level)
        if date == end_date:
            break
        else:
            date = next_month(date)

def main():
    # database name and parameters
    client = MongoClient()
    DB = client.Housing_price
    Collection = DB.Residence
    # Collection = MongoClient().Housing_price.Residence
    city_level = [1,2]
    sleep_time = 0.01
    start_date = date(2018,9,1)
    end_date = date(2018,9,1)
    driver = normal_mode()
    for citylevel in city_level:
        page_navi(Collection,citylevel,driver,sleep_time,start_date,end_date)
    driver.quit()


if __name__ == "__main__":
    main()


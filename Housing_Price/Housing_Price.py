#import and initiate driver
import time
import openpyxl
import os
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=800x600')
driver = webdriver.Chrome(executable_path='/Users/lezardvaleth/Documents/Python/chromedriver',chrome_options=options)
os.chdir('/Users/lezardvaleth/Documents/Python/Housing_Price')

lv = [1,2]
years = ['07','08','09',10,11,12,13,14,15,16,17,18]
op_count = 1
error_count = 1

wait_time = 1
date = []
name =[]
price =[]
#get data
for l in lv:
    for y in years:
        for m in range(12):
            driver.get('http://www.creprice.cn/rank/cityforsale.html?type=11&y=20'+str(y)+'&m='+str(m+1)+'&citylevel='+str(l))
            time.sleep(wait_time)
            try:
                for i in range(20):
                    name.append(driver.find_elements_by_xpath('//*[@id="order_f"]/tr['+str(i+1)+']/td[2]/a')[0].text)
                    price.append(driver.find_element_by_xpath('//*[@id="order_f"]/tr['+str(i+1)+']/td[3]').text)
                    date.append('20'+str(y)+'-'+str(m+1))
                    print(str(op_count))
                    op_count += 1
            except IndexError:
                print('Error Count =' + str(error_count))
                error_count += 1
                pass
    #write data
    file = openpyxl.load_workbook('Housing_Price.xlsx')
    sheet_p = file.get_sheet_by_name('lv'+str(l))
    try:
        for i in range(9999):
            sheet_p['A'+str(i+1)] = date[i]
            sheet_p['B'+str(i+1)] = name[i]
            sheet_p['C'+str(i+1)] = price[i]
    except IndexError:
        pass
    file.save('Housing_Price.xlsx')
    date = []
    name =[]
    price =[]

#quit browser
driver.quit()

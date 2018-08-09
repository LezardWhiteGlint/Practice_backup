#import and initiate driver
import time
import openpyxl
import os
from selenium import webdriver
driver = webdriver.Chrome(executable_path='/Users/lezardvaleth/Documents/Python/chromedriver')
os.chdir('/Users/lezardvaleth/Documents/Python/Mobile_Revenue')

month = [1,2,3,4,5,6,7,8,9]

#login in data backend
driver.get('http://acc.r2games.com/main/?r=site/login')
account = driver.find_element_by_name('account')
password = driver.find_element_by_name('password')
login = driver.find_elements_by_id('submit-btn')
account.send_keys('10024')
password.send_keys('yyy666')
account.submit()

#build a data extractor
def data_extractor(wait_time):
    time.sleep(wait_time)#neceesarry waiting
    game_name =[]
    revenue =[]
    for m in month:
        try:
            for days in range(31):
                driver.get('http://data.r2games.com/platform/?r=complex%2Frank&m=M309&p=r2games&time=2017-'+str(m)+'-'+str(days+1))
                time.sleep(wait_time)
                print(str(m)+'+'+str(days))
                for i in range(5):
                    game_name.append(driver.find_elements_by_xpath('//*[@id="__t_grid_1"]/tbody/tr['+str(i+2)+']/td[2]')[0].text)
                    revenue.append(driver.find_elements_by_xpath('//*[@id="__t_grid_1"]/tbody/tr['+str(i+2)+']/td[3]')[0].text)
        except IndexError:
            continue
    return game_name,revenue

def data_writer(row,starting_row):
    file = openpyxl.load_workbook('revenue.xlsx')
    sheet_r = file.get_sheet_by_name('Revenue')
    for i in range(row):
        try:
            #sheet_r['A'+str(i+1+starting_row)] = date[i]
            sheet_r['B'+str(i+1+starting_row)] = game_name[i]
            sheet_r['C'+str(i+1+starting_row)] = revenue[i]
        except IndexError:
            continue
    file.save('revenue.xlsx')

#excution start
#generate date list
#file = openpyxl.load_workbook('revenue.xlsx')
#sheet_d = file.get_sheet_by_name('Date')   
#date = []
#for i in range(166):
#    for q in range(5):
#        date.append(sheet_d['A'+str(i+1)].value)

#months = {1:31,2:28,3:31,4:30,5:31,6:15}

#game_name,revenue = data_extractor(1,31,1)
#data_writer(155,0)

#game_name,revenue = data_extractor(2,28,1)
#data_writer(140,155)

#game_name,revenue = data_extractor(3,31,1)
#data_writer(155,295)

#game_name,revenue = data_extractor(4,30,1)
#data_writer(150,450)

#game_name,revenue = data_extractor(5,31,1)
#data_writer(155,600)

#game_name,revenue = data_extractor(6,31,1)
#data_writer(80,755)

game_name,revenue = data_extractor(1)
data_writer(1400,0)

#quit browser
driver.quit()

#import requests
import sys
from lxml import html
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'http://acc.r2games.com/main/?r=site/ajaxLogin'



#s = requests.session()
login_data = {
    "account":"sheldon@r2games.com",
    "password":"yyy666",
    "lang":"zh_cn"
        }
r = s.post(url, data = login_data)
wrt = s.get("http://data.r2games.com/platform/?r=complex%2Findex&m=M273&p=r2games&g=wartune&server=ALL&time_start=2017-04-22&time_end=2017-05-22&show=ByDate")
#tree = html.fromstring(wrt.content)
#recharge = tree.xpath('//table/tbody/tr[1]/td[8]/text()')
#print(recharge)


data = wrt.text
soup = BeautifulSoup(data,"html.parser")




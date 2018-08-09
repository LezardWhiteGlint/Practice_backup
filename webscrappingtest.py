import requests
from bs4 import BeautifulSoup

url = 'http://www.creprice.cn/rank/cityforsale.html?type=11&citylevel=2&y=2017&m=04'


s = requests.session()

price = s.get(url)

data = price.text
soup = BeautifulSoup(data,"html.parser")
form = soup.find('tbody')
form_strip = form.stripped_strings
data = form('td')





#from __future__ import division, unicode_literals
#import codecs
import io
import os
import sys
import re
from datetime import datetime
from bs4 import BeautifulSoup
#abspath = os.path.abspath(__file__)
#dname = os.path.dirname(abspath)
#os.chdir(dname)

if getattr(sys,'frozen',False):
    application_path = sys._MEIPASS
     # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

print(application_path)

time_date = []
time = []
date = []
status = []
time_cal = []

#filename = 'sample1.html'
filename = os.path.join(application_path, 'sample.html')


#get table content
def table(filename):
    file = io.open(filename,'r',encoding='GBK')
    soup = BeautifulSoup(file, 'html.parser')
    table = soup.find('table', id='GridView1')
    rows = table.find_all('td')
    content = []
    for r in rows:
            content.append(r.get_text())
    return content

#put content into lists
def split(content):
    for ele in content:
        if len(ele) > 15:
            time_date.append(ele)
        if ele == 'Check In' or ele == 'Check Out':
            status.append(ele)
        if len(ele) > 3 and len(ele) < 15 and ele != 'Check In' and ele != 'Check Out' :
            date.append(ele)

    #get time only list
    for t in time_date:
        time.append(t.split()[1])
        print(t.split()[0])

    #parse time list and convert them into seconds
    for t in time:
        FMT = '%H:%M:%S'
        time_temp = datetime.strptime(t, FMT)
        seconds = time_temp.hour * 3600 + time_temp.minute * 60 + time_temp.second
        time_cal.append(seconds)
    return time_cal

#caculate total time and display
def total_time(time_cal):
    total_time = 0
    try:
        for i in range(len(time_cal)):
            if time_cal[i] < time_cal[i+1]:
                total_time = total_time + time_cal[i+1] - time_cal[i]
    except IndexError:
        pass
    return total_time

def display(total_time):
    hours = total_time //3600
    minutes = (total_time-hours*3600)//60
    seconds = total_time - hours*3600 - minutes*60
    print('------------------working hours-----------------')
    print('------------------working hours-----------------')
    print('------------------working hours-----------------')
    print(str(hours)+':'+str(minutes)+':'+str(seconds))
    print('------------------working hours-----------------')
    print('------------------working hours-----------------')
    print('------------------working hours-----------------')


def app():
    content = table(filename)
    time_cal = split(content)
    time_result = total_time(time_cal)
    display(time_result)

app()
    


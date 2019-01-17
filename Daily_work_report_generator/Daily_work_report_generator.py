#!/Usr/bin/env python3
from datetime import datetime,timedelta

today = datetime.today()

weekday = today.weekday()

if weekday == 0:
    print('1. 更新EZPZ公告')
    print('2. 参与周会')

if weekday == 1:
    print('1. 准备ezpz下周活动')

if weekday == 2:
    print('1. 提交ezpz下周活动给研发')

if weekday == 3:
    print('Nothing for today')

if weekday == 4:
    print('1. 更新ezpz公告')
    print('2. 出周报并发送给ice')

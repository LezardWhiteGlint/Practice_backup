import arrow
import datetime

#use arrow to generate date automaticly
backend_date = arrow.now() - datetime.timedelta(days=2)

year = backend_date.format('YYYY')
month = backend_date.format('MM')
last_month = str(int(month)-1)



#determing date range
time_start = backend_date.format('YYYY-MM')+'-01'
time_end = backend_date.format('YYYY-MM-DD')
time_start_last_month = year+'-'+last_month+'-01'
time_end_last_month = year+'-'+last_month+'-'+backend_date.format('DD')

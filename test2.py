def ulti_display(weeklist,daily_h,date):
    total = 0
    data = []
    message = []
    for weekday in weeklist:
        for i in range(len(date)):
           if weekday == date[i]:
               data.append(daily_h[i])
               total = total + daily_h[i]
    #print "<html><body>"
    for i in data:
        hours = int(i/2)
        minutes = int(i%2)*30
        message.append(str(hours)+':'+str(minutes))
    total_h = int(total/2)
    total_m = int(total%2)*30
    totoal_message = str(total_h)+':'+str(total_m)
    try:
        for i in range(len(weekday)):
            print('<p>Date: '+weekday[i]+'-------'+message[i]+'</p>')
            print "\n"
            print('<p>This Week Total: '+weekday[i]+'-------'+data[i]+'</p>')
    except: IndexError
    # print "</body></html>"

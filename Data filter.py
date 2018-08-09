def listgenerator():
    import random
    global listbefore
    listbefore = []
    for i in range(0,10):
        num = random.randint(1,100)
        listbefore = listbefore + [num]
    print('It is the initial list')
    print(str(listbefore))
       
def list_filter():
    global listafterbig
    global listaftersmall
    listafterbig = []
    listaftersmall = []
    for num in range(len(listbefore)):
        if listbefore[num] > 50:
            listafterbig = listafterbig + [listbefore[num]]
        else:
            listaftersmall = listaftersmall + [listbefore[num]]

listgenerator()
list_filter()
print('numbers larger than 50')
print(listafterbig)
print('numbers lesser or equal to 50')
print(listaftersmall)

import openpyxl
from pymongo import MongoClient
import pymongo


def hard_labor(Collection_name,file_name):
    client = MongoClient()
    DB = client.Mobile_revenue
    Collection = DB[Collection_name]


    file = openpyxl.load_workbook(file_name)
    sheet = file.get_sheet_by_name('Sheet')
    result = Collection.find({'date':{'$gt':'2018-08-00'}})
    result = result.sort('date', pymongo.ASCENDING)

    i=1
    for item in result:
        sheet['A'+str(i)]=item['date']
        sheet['B'+str(i)]=item['dau']
        i +=1

    file.save(file_name)

hard_labor('EZ_PZ_RPG_3D','dau_en.xlsx')
hard_labor('EZ_PZ_RPG_3D_RU','dau_ru.xlsx')

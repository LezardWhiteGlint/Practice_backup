from datetime import date as datetime

class record(object):
    def __init__(self,price, classfication,date,comment):
        assert type(price) == int or type(price) == float
        assert type(classfication) == str
        assert type(date) == datetime
        assert type(comment) == str
        self.price = price
        self.classfication = classfication
        self.date = date
        self.comment = comment
        

    def getPrice(self):
        return self.price

    def getClass(self):
        return self.classfication

    def getDate(self):
        return self.date

    def getComment(self):
        return self.comment

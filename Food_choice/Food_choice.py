import random

class Food(object):
    def __init__(self,header,info):
        '''
            header : a list splited from the frist line of csv file 
            info : a list splited from a line of food info from interation of csv
        '''
        assert isinstance(header,list), 'header is not a list'
        assert isinstance(info,list), 'info is not a list'
        name_index = header.index('name')
        set_index = header.index('set')
        category_index = header.index('category')
        kcal_index = header.index('kcal/100g')
        gi_index = header.index('gi')
        self.name = info[name_index]
        self.set = info[set_index]
        self.category = info[category_index]
        self.portion = 0
        try:
            self.kcal = int(info[kcal_index])
        except:
            self.kcal = None
        try:
            self.gi = int(info[gi_index])
        except:
            self.gi = None

    def getName(self):
        return self.name

    def getSet(self):
        return self.set

    def getCategory(self):
        return self.category

    def getKcalPer100Gram(self):
        return self.kcal

    def getGi(self):
        return self.gi

    def getPortion(self):
        return self.portion

    def setPortion(self,num):
        assert isinstance(num,int), 'Portion need to be integer.'
        self.portion = num

    def getKcal(self):
        return self.getKcalPer100Gram()*self.getPortion()/100
        
        
#read food info from csv file


##def cat_test(foods_list):
##    for food in foods_list:
##        print(food.getName())
##    print('------------- above is ' + food.getCategory() + ' -----------')
##cat_test(carb_main)
##cat_test(carb_veg)
##cat_test(protein)
##cat_test(fat)
##print('check if anything left out')
##cat_test(other_test_only)

class DailyMeals(object):
    def __init__(self,maxTotalKcal = 1998, minTotalKcal = 1500, foodToRemove = ['bacon','sausage','beef']):
        def read_file(csv_file):
            '''
            return a list of foods
            '''
            file = open(csv_file)
            header = file.readline().split(',')
            foods_temp = []
            foods = []
            for line in file:
                info = line.split(',')
                foods_temp.append(Food(header,info))
            for food in foods_temp:
                #print(food.getName())
                if food.getName() == '':
                    continue
                else:
                    foods.append(food)
            file.close()
            return foods

        def removeFood(foodNameList):
            for i in foodNameList:
                for f in foods:
                    if f.getName() == i:
                        foods.remove(f)

        foods = read_file('Food_Table.csv')
        removeFood(foodToRemove)
##        for i in foods:
##            print(i.getName())
        #make category
        carb_main = []
        carb_veg = []
        protein = []
        fat = []
        other_test_only = []

        for food in foods:
            if food.getCategory() == 'protein':
                protein.append(food)
            elif food.getCategory() == 'fat':
                fat.append(food)
            elif food.getCategory() == 'carbonhydrate' and food.getKcal() > 100 or food.getName() == 'potato':
                carb_main.append(food)
            elif food.getCategory() == 'carbonhydrate' and food.getKcal() <= 100 and food.getName() != 'potato':
                carb_veg.append(food)
            else:
                other_test_only.append(food)
        self.foods = foods
        self.main = carb_main
        self.veg = carb_veg
        self.protein = protein
        self.fat = fat
        self.maxTotalKcal = maxTotalKcal
        self.minTotalKcal = minTotalKcal
        self.breakfast = []
        self.lunch = []
        self.dinner = []

    def addFood(self,foodName,targetList,portion):
        assert isinstance(foodName,str), 'Food name need to be string.'
        check = False
        for i in self.foods:
            if i.getName() == foodName:
                i.setPortion(portion)
                targetList.append(i)
                #targetList.remove(i)
                check = True
        if check == False:
            raise ValueError('There is no such food in list.')

    def getAllFoodsName(self):
        result = []
        for i in self.foods:
            result.append(i.getName())
        return result

    def addBreakfast(self,foodName,portion):
        self.addFood(foodName,self.breakfast,portion)

    def addLunch(self,foodName,portion):
        self.addFood(foodName,self.lunch,portion)

    def addDinner(self,foodName,portion):
        self.addFood(foodName,self.dinner,portion)

    def getBreakfast(self):
        return self.breakfast

    def getLunch(self):
        return self.lunch

    def getDinner(self):
        return self.dinner

    def getDailyFoods(self):
        return self.breakfast + self.lunch + self.dinner

    def getTotalKcal(self,foodList):
        total = 0
        for i in foodList:
            total += i.getKcal()
        return total

    def getDailyKcal(self):
        return self.getTotalKcal(self.getDailyFood())


    

##    def getKcal(self,foodName):
##        assert isinstance(foodName,str), 'Food name need to be string.'
##        for i in self.foods:
##            if i.getName() == foodName:
##                return i.getKcal()
##        raise ValueError('There is no such food in list.')

    def autoChooseFood(self,category,kcal):
        while True:
            print('------------------category food list ---------')
            for i in category:
                print(i.getName())
            print('-----------------end of category list----------')
            food = random.choice(category)
            portion = kcal/food.getKcalPer100Gram()
            if portion >= 1:
                category.remove(food)
                return (food, int(portion*100))
            else:
                continue

    def generateBreakfast(self,Kcal=300):
        self.addBreakfast('egg',60)
        self.addBreakfast('oat',50)
        self.addBreakfast('milk',100)
        target = self.protein[:]
        for f in target:
            if f.getName() == 'egg' or f.getName() == 'milk':
                self.protein.remove(f)
##        for f in self.protein:
##            if f.getName() == 'egg' or f.getName() == 'milk':
##                self.protein.remove(f)
##                print('removeddddd egg')
##            if f.getName() == 'milk':
##                self.protein.remove(f)
##                print('removedddddd milk')
        for f in self.protein:
            print(f.getName())

    def generateLunch(self,Kcal=700):
        self.addLunch('rice(raw)',80)
        food,portion = self.autoChooseFood(self.protein,Kcal - self.getTotalKcal(self.lunch))
        self.addLunch(food.getName(),portion)

    def generateDinner(self,Kcal=500):
        self.addLunch('noodle(boiled)',70)
        food,portion = self.autoChooseFood(self.protein,Kcal - self.getTotalKcal(self.dinner))
        self.addLunch(food.getName(),portion)

test = DailyMeals()
test.generateBreakfast()
test.generateLunch()
test.generateDinner()
print(test.getTotalKcal(test.getDailyFoods()))
foods = test.getDailyFoods()
for f in foods:
    print(f.getName())
    print(f.getPortion())

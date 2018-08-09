def numgenerator():
    import random
    global targetnum
    targetnum = random.randint(1,100)

def input_and_checknum():
    while True:
        num=input()
        num=int(num)
        if num < targetnum:
            print('too low')
        elif num > targetnum:
            print('too high')
        elif num == targetnum:
            print('Congratulations, you are right.')
            break

numgenerator()
print('Try to guess the number')
input_and_checknum()




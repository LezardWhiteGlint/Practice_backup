'''Question:
McDonald’s sells Chicken McNuggets in packages of 6, 9 or 20 McNuggets.
Thus, it is possible, for example, to buy exactly 15 McNuggets
(with one package of 6 and a second package of 9),
but it is not possible to buy exactly 16 McNuggets,
since no non- negative integer combination of 6's, 9's and 20's
add up to 16. To determine if it is possible to buy exactly n McNuggets,
one has to find non-negative integer (can be 0) values of a, b,
and c such that

6a+9b+20c=n
Write a function, called McNuggets that takes one argument,
n, and returns True if it is possible to buy a combination of
6, 9 and 20 pack units such that the total number of McNuggets equals n,
and otherwise returns False. Hint: use a guess and check approach.'''

n = [5,6,8,9,14,15,30,20,40,100,200,300,400,500,600,11,12,21,32,41,23,13]

def test(n):
    for i in n:
        print(i)
        print(solution2(i))
        print('----')

def solution1(n):
    status = False
    for a in range(int(n/6+1)):
        for b in range(int(n/9+1)):
            for c in range(int(n/20+1)):
                if 6*a + 9*b + 20*c == n:
                    status = True
    return status

def solution2(n):
    status = False
    if n%6 == 0 or n%9 == 0 or n%20 == 0:
        status = True
    elif n%20 != 0 and n > 20:
        status = solution2(n-20)
    elif n%9 != 0 and n > 9:
        status = solution2(n-9)
    elif n%6 !=0 and n > 6:
        status = solution2(n-6)
    return status

balance = 3926
annualInterestRate = 0.2

b = balance
r = annualInterestRate

p = 10


while True:
    ub = b
    for m in range(12):
        ub = ub - p
        ub = ub + (r/12)*ub
        #print(ub)
    if ub <= 0:
        break
    p += 10
    #print('p = '+str(p))

print('Lowest Payment: '+str(p))
    

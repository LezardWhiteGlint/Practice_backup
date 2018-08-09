balance = 999999
annualInterestRate = 0.18

b = balance
r = annualInterestRate

mr = r/12
mplb = b/12
mpub = (b*(1+mr)**12)/12

p = (mplb+mpub)/2


while True:
    ub = b
    for m in range(12):
        ub = ub - p
        ub = ub + (r/12)*ub
        #print(ub)
    if ub < 0:
        mpub = p
    if ub > 0:
        mplb = p
    if round(ub,2) == 0:
        break
    p = (mplb+mpub)/2
    #print('p = '+str(p))

print('Lowest Payment: '+str(round(p,2)))
    

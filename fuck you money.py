# This program says fuck you and ask for your fuck you money goal.
print('Fuck you')
fuck_you_money_goal=1200000
initial_investment=400000
long_term_interest_rate=0.03 #real interest, ignore inflation
save_each_year=100000
save_each_year=int(save_each_year)
years_left=1
asset=initial_investment*(1+long_term_interest_rate)+save_each_year*years_left
while asset < fuck_you_money_goal:
    years_left=years_left+1
    asset=asset*(1+long_term_interest_rate)+save_each_year
print('Your need to work '+str(years_left)+' more years')
print('Your assest value will be '+str(asset))




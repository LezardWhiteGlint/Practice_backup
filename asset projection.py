initial_investment=400000
long_term_interest_rate=0.03 #real interest, ignore inflation
save_each_year=100000
asset=initial_investment
for year in range(2016,2031):
    asset=asset*(1+long_term_interest_rate)+save_each_year
    print('Your asset at the end of ' + str(year) + ' is ' + str(asset))
    




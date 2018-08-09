#data conditions
monthly_invest_amount = 1000
asset_goal = 5000000
annualy_return_guess = 0.05
monthly_return_guess = annualy_return_guess/12

def return_guess(monthly_invest_amount):
    while True:
        total_asset = 0
        for m in range(240):
            current_asset = monthly_invest_amount + total_asset*(1+monthly_return_guess)
            total_asset = current_asset
            #print(current_asset)
        if current_asset > asset_goal:
            print('monthly investment amount should be ' + str(monthly_invest_amount))
            break
        else:
            monthly_invest_amount += 500

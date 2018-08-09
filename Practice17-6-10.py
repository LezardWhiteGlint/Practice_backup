#small game, elif testing

print('You have some games to select.'
      '\n1. Zelda'
     '\n2. EVE'
      '\n3. Monster Hunter'
      '\nWhich one are you going to play?')

ns_off = True


while True:
    print('Tell me your selection')
    select = input()
    if select == '1' and ns_off:
        print('Turn on your NS')
        ns_off = False
    elif select =='1' and not ns_off:
        print('Zelda initiated, get ready to have fun.')
        break
        

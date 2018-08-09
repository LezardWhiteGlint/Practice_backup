high = 100
low = 0

print('Please think of a number between 0 and 100!')

while True:
    guess =  int((high + low)/2)
    print('Is your secret number '+ str(guess))
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans == 'h':
        high = guess
    elif ans == 'l':
        low = guess
    elif ans == 'c':
        print('Game over. Your secret number was: ' + str(guess))
        break
    else:
        print('Please input the currect answer as stated.')

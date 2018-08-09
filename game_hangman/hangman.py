import random
import sys
import os
ava_words = 'abcdefghijklmnopqrstuvwxyz'
guesscount = 8
display = ''
wordgoal = 'fuck'
"""
1. get a wordgoal

following are a loop:
2. show how many guesses left, return guesscount 
3. show available letter left, return available letter,
and check the if the input is in the avaliable letter and return a status
4. input a guess letter
5. display guess result
6. change guesscount

if guesscount = 0 ,lose, quit
if guess all the letter, win, quit

"""

if getattr(sys,'frozen',False):
    application_path = sys._MEIPASS
     # If the application is run as a bundle, the pyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app 
    # path into variable _MEIPASS'.
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

os.chdir(application_path)

#get the wordlist
def words_list():
    file = open('words.txt')
    line = []
    for l in file:
        line.append(l)
    wordslist = line[0]
    print('Words base loading complete.')
    return wordslist.split(' ')


#generate a new word for guess
def word_goal(wordslist):
    wordgoal = random.choice(wordslist)
    print('Target is a ' + str(len(wordgoal)) + ' characters word.')
    return wordgoal

#display availiable words
def avaliable_words(input_word,ava_words):
    each = []
    for i in ava_words:
        each.append(i)
    if input_word in each:
        ava_words = ava_words.replace(input_word,'_')
        print('The avaliable words are ' + ava_words)
        status = True
    if input_word not in each:       
        print('You have already guessed that letter.')
        print('The avaliable words are ' + ava_words)
        status = False
    return ava_words,status

def word_input():
    input_word = input('input your guess here:')
    return input_word

#guess left count
def guess_count(guesscount,status,check):
    if status == True and check == False:
        guesscount -= 1
        print('You have ' + str(guesscount) +' guess left')
    else:
        print('You have ' + str(guesscount) +' guess left')
    return guesscount



#check if the word is correct, and output the already guessed word
def word_check(wordguess,wordgoal):
    each = []
    display = []
    result = ''
    check = False
    for i in wordgoal:
        each.append(i)
    for char in each:
        if char == wordguess:
            display.append(wordguess)
            check = True
        else:
            display.append('_')
    for i in display:
        result = result + str(i)
    return result,check

#check if the game meets the end
def end_check(guesscount,display,wordgoal):
    endcheck = 0
    if guesscount == 0 and display != wordgoal:
        endcheck = 1
        print('You run out of guesses, game over.')
    if display == wordgoal:
        endcheck = 2
        print('Congratulations, you win.')
    return endcheck

wordslist = words_list()
wordgoal = word_goal(wordslist)
for i in wordgoal:
    display = display + '_'
print('You have ' + str(guesscount) +' guesses left.')
print('Available letters: abcdefghijklmnopqrstuvwxyz')

while True:
    input_word = word_input()
    ava_words,status = avaliable_words(input_word,ava_words)
    result,check = word_check(input_word, wordgoal)
    guesscount = guess_count(guesscount,status,check)
    displaylist = list(display)#make the result list so it can be changed
    resultlist = list(result)
    for i in range(len(resultlist)): #make sure the _ won't replace the guessed words
        if resultlist[i] != '_':
            displaylist[i] = resultlist[i]
    display = ''.join(displaylist)
    print('Your guess progress: ' + display)

    endcheck = end_check(guesscount,display,wordgoal)
    if endcheck == 1:
        print('The correct answeser is '+ wordgoal)
        break
    if endcheck == 2:
        break


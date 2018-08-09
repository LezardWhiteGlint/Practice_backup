vowel = ['a','A','e','E','i','I','o','O','u','U']
def isVowel(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    # Your code here
    vowel = ['a','A','e','E','i','I','o','O','u','U']
    check = 0
    for c in vowel:
        if char == c:
            check +=1
    if check == 1:
        return True
    else: return False

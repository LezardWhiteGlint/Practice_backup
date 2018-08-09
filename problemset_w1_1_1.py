length = len(s)
count = 0
try:
    for i in range(length):
        if s[i] == 'b':
            if s[i+1] == 'o':
                if s[i+2] == 'b':
                    count +=1
except IndexError:
    pass
print('Number of times bob occurs is: '+ str(count))

s='abcdefghijklmnopqrstuvwxyz'
s = s + ' '


def seq_definer():
    seq =''
    result = []
    try:
        for c in range(len(s)):
            for i in range(len(chars)):      
                while True:
                    if chars[i] == s[c]:
                        seq = seq + s[c]
                    i += 1
    except IndexError:
        pass
    return result

def char_check():
    seq=''
    record = []
    try:
        for anker in range(len(s)):
            print(anker)
            for i in range(len(chars)):
                if chars[i] == s[anker]:
                    seq = seq + chars[i] #record the character
            record.append(seq)
            print(seq)
            seq=''
    except IndexError:
        pass
    return record

def third_try():
    seq = ''
    record = []
    try:
        for i in range(len(s)):
            if seq == '':
                    seq = s[i]
            if s[i] <= s[i+1]:
                seq = seq + s[i+1]
            else:
                record.append(seq)
                seq = ''
    except IndexError:
        pass
    return record

def compare(a,b):
    if len(a) >= len(b):
        return a
    if len(a) < len(b):
        return b

result = third_try()
winner = result[0]
for i in range(len(result)):
    try:
        b = result[i+1]
        winner = compare(winner,b)
    except IndexError:
        pass
print('Longest substring in alphabetical order is: '+ winner)
        
        

            
        

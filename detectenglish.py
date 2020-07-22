upperletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = upperletters + upperletters.lower() + ' \t\n'

def loaddict():
    fo = open('dictionary.txt')
    words = {}
    for word in fo.read().split('\n'):
        words[word] = None
    fo.close()
    return words

engwords = loaddict()

def cleantext(msg):
    l1 = []
    for i in msg:
        if i in letters:
            l1.append(i)
    return ''.join(l1)

def engcount(msg):
    possiblewords = cleantext(msg.upper()).split()
    if possiblewords == []:
        return 0.0
    count = 0
    for word in possiblewords:
        if word in engwords:
            count += 1
    return float(count)/len(possiblewords)

def isenglish(msg, wordper=20, letterper=85):
    wordmatch = engcount(msg)*100 >= wordper
    lettermatch = float(len(cleantext(msg)))/len(msg)*100 >= letterper
    return wordmatch and lettermatch
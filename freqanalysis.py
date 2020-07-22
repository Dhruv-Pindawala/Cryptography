engfreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

etaoin = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def lettercount(msg1):
    lcount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for letter in msg1():
        if letter in letters:
            lcount[letter] += 1
    return lcount

def freqorder(msg1):
    ltof = lettercount(msg1)
    ftol = {}

    for letter in letters:
        if ltof[letter] not in ftol:
            ftol[ltof[letter]] = [letter]
        else:
            ftol[ltof[letter]].append(letter)
    
    for freq in ftol:
        ftol[freq].sort(key=etaoin.find, reverse=True)
        ftol[freq] = ''.join(ftol[freq])
    
    freqpair = list(ftol.items())
    freqpair.sort(key = lambda x : x[0], reverse = True)

    freqlist = []
    for frq in freqpair:
        freqlist.append(frq[1])
    return ''.join(freqlist)

def matchscore(msg1):
    order = freqorder(msg1)
    scoore = 0

    for i in etaoin[:6]:
        if i in order[:6]:
            score += 1
    for j in etaoin[-6:]:
        if j in order[-6:]:
            score += 1

    return score
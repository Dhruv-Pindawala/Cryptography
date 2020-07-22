# NOTE = THIS METHOD WILL WORK ONLY WHEN THE ENCRYPTED LETTERS ARE ALPHATES AND NOT ANY OTHER CHARACTER......

import re, copy, pprint, makingwordpatterns, wordpatterns

letters = 'ABCDEFGHIJKLNOPQRSTUVWXYZ'
nonlettersorspacepattern = re.compile('[^A-Z\s]')

msg = input('enter the text : ')

def main(msg2):
    print()
    print('hacking under process......')
    lettermapping = hacksimplesub(msg2)

    print('mapping or decryption key :')
    pprint.pprint(lettermapping)
    
    hackedmsg = decryptcypher(msg, lettermapping)

    print(hackedmsg)

def blankcipher():
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

def addletter(lettermapping, cipherword, candidate):
    lettermapping = copy.deepcopy(lettermapping)
    for i in range(len(cipherword)):
        if candidate[i] not in lettermapping[cipherword[i]]:
            lettermapping[cipherword[i]].append(candidate[i])
        return lettermapping

def intermapping(mapa, mapb):
    intermap = blankcipher()

    for j in letters:
        if mapa[j] == []:
            intermap[j] = copy.deepcopy(mapb[j])
        elif mapb[j] == []:
            intermap[j] = copy.deepcopy(mapa[j])
        else:
            for k in mapa[j]:
                if k in mapb[j]:
                    intermap[j].append(k)
    return intermap

def removeletter(letmap):
    letmap1 = copy.deepcopy(letmap)
    loop = True
    while loop:
        loop = False
        solvedletter = []
        for cilet in letters:
            if len(letmap1[cilet]) == 1:
                solvedletter.append(letmap1[cilet][0])
        
        for cilet in letters:
            for s in solvedletter:
                if len(letmap1[cilet]) != 1 and s in letmap1[cilet]:
                    letmap1[cilet].remove(s)
                    if len(letmap1[cilet]) == 1:
                        loop = True
    return letmap1

def hacksimplesub(msg1):
    intermap = blankcipher()
    ciwordlist = nonlettersorspacepattern.sub('', msg1.upper()).split()
    for ciw in ciwordlist:
        map = blankcipher()
        wordpattern = makingwordpatterns.wordpattern(ciw)
        if wordpattern not in wordpatterns.patterns:
            continue

        for cand in wordpatterns.patterns[wordpattern]:
            map = addletter(map, ciw, cand)
        
        intermap = intermapping(intermap, map)
    return removeletter(intermap)

def decryptcypher(citext, lettermapping):
    key = ['x'] * len(letters)
    for cilet in letters:
        if len(lettermapping[cilet]) == 1:
            keyindex = letters.find(lettermapping[cilet][0])
            key[keyindex] = cilet
        else:
            citext = citext.replace(cilet.lower(), '_')
            citext = citext.replace(cilet.upper(), '_')
    key = ''.join(key)

    return translatemsg(key, citext)

def translatemsg(key, msg):
    tran = ''
    chara, charb = key, letters
    for sy in msg:
        if sy.upper() in chara:
            symindex = chara.find(sy.upper())
            if sy.isupper():
                tran += charb[symindex].upper()
            else:
                tran += charb[symindex].lower()
        else:
            tran += sy
    return tran

if __name__ == '__main__':
    main(msg)
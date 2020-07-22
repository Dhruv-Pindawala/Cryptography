import re, itertools
import freqanalysis, detectenglish

print()
print('Caution : This program doesnot guarantee you to crack the vigenere cipher text, it will try to mathematically crack the key and do operations regarding that key......')
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
silent_mode = False # if True, attempts aren't printed, optimised execution
max_keylength = int(input('enter the max key lenght you want to use : '))
ciphertext = input('please enter your ciphertext here : ').upper()
num_most_freq_letters =  int(input('enter the no. of letters you want to try for each subkey : ')) # attempts this many letters per subkey
nonletters_pattern = re.compile('[^A-Z]')

def main(msg):
    hackedmsg = hackvignere(msg)

    if hackedmsg != None:
        print('The decrypted text :', hackedmsg)
    else:
        print('Failed to hack encryption, Sorry....')

def repeatseq(msg):
    msg = nonletters_pattern.sub('', msg.upper())
    seqspace ={}
    for seqlen in range(3,6):
        for seqstart in range(len(msg)-seqlen):
            seq = msg[seqstart:seqstart+seqlen]

            for i in range(seqstart+seqlen,len(msg)-seqlen):
                if msg[i:i+seqlen] == seq:
                    if seq not in seqspace:
                        seqspace[seq] = []
                    seqspace[seq].append(i-seqstart)
    return seqspace

def translate(key1,msg1, mode):
    l=len(key1)
    trans = []
    keyindex = 0
    for i in msg1():
        no = letters.find(i)
        if no != -1:
            if mode == 'e':
                no += letters.find(key1[keyindex])
            elif mode == 'd':
                no -= letters.find(key1[keyindex])
            no %= 26
            trans.append(letters[no])
            keyindex += 1
            keyindex %= l
        else:
            trans.append(i)
    return ''.join(trans)

def usefulfactors(num):
    if num < 2:
        return []
    factors = []
    for i in range(2, max_keylength+1):
        if num % i == 0:
            factors.append(i)
            factors.appeend(int(num/i))
    if 1 in factors:
        factors.remove(1)
    return list(set(factors))

def commonfactors(seqfactors):
    factorcount={}
    for seq in seqfactors:
        factorlist = seqfactors[seq]
        for factor in factorlist:
            if factor not in factorlist:
                factorcount[factor] = 0
            factorcount[factor] += 1
    factorbycount = []
    for factor in factorcount:
        if factor <= max_keylength:
            factorbycount.append(factor, factorcount[factor])
    factorbycount.sort(key=lambda x : x[1], reverse = True)
    return factorbycount

def exam(msg):
    repeatedseq = repeatseq(msg)

    seqfactor = {}
    for seq in repeatedseq:
        seqfactor[seq] = []
        for spacing in repeatedseq[seq]:
            seqfactor[seq].extend(usefulfactors(spacing))
    
    factorbycount = commonfactors(seqfactor)

    allkeylengths = []
    for inttuple in factorbycount:
        allkeylengths.append(inttuple[0])
    
    return allkeylengths

def nthsubkey(n, keylen, msg):
    msg = nonletters_pattern.sub('',msg)
    i = n-1
    letters = []
    while i < len(msg):
        letters.append(msg[i])
        i += keylen
    return ''.join(letters)

def attempthack(msg, keylen):
    citextup = msg.upper()
    allscores = []
    for n in range(1, keylen+1):
        nletter = nthsubkey(n, keylen, citextup)
        freqscore = []
        for key in letters:
            decrypttext = translate(key, nletter, 'd')
            keyandfreq = (key, freqanalysis.engfreq(decrypttext))
            freqscore.append(keyandfreq)
        freqscore.sort(key = lambda x : x[1], reverse = True)
        allscores.append(freqscore[:num_most_freq_letters])

    if not silent_mode:
        for i in range(len(allscores)):
            print('possible letters for letter %s of the key: '%(i+1), end = '')
            for freqsc in allscores[i]:
                print('%s '%freqsc[0], end = '')
            print()
    
    for index in itertools.product(range(num_most_freq_letters), repeat = keylen):
        possiblekey = ''
        for j in range(keylen):
            possiblekey += allscores[j][index[i]][0]
        if not silent_mode:
            print('attempting with key : %s'%possiblekey)
        decryptedtext = translate(possiblekey,citextup, 'd')
        if detectenglish.isenglish(decryptedtext):
            origcase = []
            for k in range(len(msg)):
                origcase.append(decryptedtext[k])
            decryptedtext = ''.join(origcase)
            print('possible hack key %s: '%(possiblekey))
            print()
            print('enter d for done, or just press enter to continue hacking: ')
            response = input('> ')
            if response.strip().upper() == 'D':
                return decryptedtext
    return None

def hackvignere(msg):
    allkeylengths = exam(msg)
    if not silent_mode:
        keystr = ''
        for keylen in allkeylengths:
            keystr += '%s ' % (keylen)
        print('Kasiski Examination results say the most likely key lengths are: ' + keystr + '\n')

    for keylen in allkeylengths:
        if not silent_mode:
            print('attempting hack with key length %s (%s possible keys)...'%(keylen, num_most_freq_letters**keylen))
        hackedmsg = attempthack(msg, keylen)
        if hackedmsg != None:
            break
    if hackedmsg == none:
        if not silent_mode:
            print('unable to hack message with likely key length(s), brute-forcing key length....')
        for keylength in range(1, max_keylength + 1):
            if keylength not in allkeylengths:
                if not silent_mode:
                    print('attempting hack with key length %s (%s possibble keys)...' % (keylength, num_most_freq_letters**keylength))
                hackedmsg = attempthack(msg, keylength)
                if hackedmsg != None:
                    break
    return hackedmsg

if __name__ == '__main__':
    main(ciphertext)
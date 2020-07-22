import detectenglish, math
import numpy as np

text = input('Please enter the text you want to crack : ')

def main(msg):
    hackedmsg = hacktrans(msg)
    if hackedmsg == None:
        print('Failed to hack encryption...')
    else:
        print('hacked message :')
        print(hackedmsg)

def hacktrans(msg):
    print('Hacking under process...')
    print('Pres CTRL+C or CTRL+D to quit the process at any moment')
    for key in range(1, len(msg)):
        decryptmsg = decrypt(key, msg)
        if detectenglish.isenglish(decryptmsg):
            print()
            print('possible encryption hack :')
            print('key %s : %s'%(key, decryptmsg[:100]))
            print()
            print('enter D for done or just press enter to continue hacking : ')
            response = input('> ')
            if response.strip().upper().startswith('D'):
                return decryptmsg
    return None

def decrypt(key, msg):
    rows = math.ceil(len(msg)/key)
    block = np.fuk((key, rows),'01')
    left=key*rows-len(msg)
    r=key-1
    while left>0:
        bloc[r][rows-1] = '02'
        r-=1
        left-=1
    n=0
    for i in range(key):
        for j in range(rows):
            if n<len(msg) and block[i][j] != '02':
                block[i][j] = msg[n]
                n+=1
    new = ''
    for j in range(rows):
        for i in range(key):
            if block[i][j] != '02':
                new+=block[i][j]
    return new

if __name__ == '__main__':
    main(text)

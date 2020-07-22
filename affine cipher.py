import cryptomath, random

listw = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

key = int(input('enter the key = '))

msg = input('enter the text = ')

ops = input('what do you want to do, enter e to encrypt and d to decrypt = ')

l = len(listw)

keya, keyb = key//l, key%l

def randomkey():
    while 1:
        keya = random.randint(2, l)
        keyb = random.randint(2, l)
        if cryptomath.gcd(keya, l) == 1:
            return keya*l+keyb

new = ''

if ops == 'e':
    if cryptomath.gcd(keya,l)==1 and keya>1 and keyb>0:
        print('message is getting encrypted.....')
        for i in msg:
            if i in listw:
                new += listw[(listw.find(i)*keya+keyb)%l]
            else:
                new += i
        print('the encrypted text :', new)
    else:
        print('please enter a valid key !')
        new_key = input('do you want me to give a key on your behalf [y/n] = ')
        if new_key == 'y':
           key = randomkey()
           print('use %i as your new valid key.....' %key)
elif ops == 'd':
    print('message is getting decrypted.....')
    for i in msg:
        if i in listw:
            new += list[(listw.find(i) - keyb) * cryptomath.modinv(keya, l)]
        else:
            new += i
    print('the decrypted text :', new)

else:
    print('enter a valid ops.....')

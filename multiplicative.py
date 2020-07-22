import cryptomath

key = int(input('enter the key = '))

msg = input('enter the text = ').lower() #to avoid any confusion

ops = input('what do you want to do, enter e to encrypt and d to decrypt = ')

listw = 'abcdefghijklmnopqrstuvwxyz'

new = ''

if ops == 'e':
    if cryptomath.gcd(key,26) == 1:
        for i in msg:
            if i in listw:
                new += listw[(listw.index(i)*key)%26]
            else:
                new += i
        print('encrypted text :', new)
    else:
        print('enter a valid key')
    
elif ops == 'd':
    key1 = cryptomath.modinv(key,26)
    for i in msg:
        if i in listw:
            new += listw[(listw.index(i)*key1)%26]
        else:
            new += i
    print('decrypted text :', new)

else:
    print('enter a valid ops')
import sys, random

key = ''.join(list(set(list(input('enter the key, to generate one, enter y = ')))))

listw = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXY Z[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

msg = input('enter the text = ')

ops = input('what do you want to do, enter e to encrypt and d to decrypt = ')

def validkey():
    if len(key) == len(listw):
        return True
    else:
        return False

def translate(listw1 , key1):
    new = ''
    for i in msg:
        if i in listw1:
            new += key1[listw1.find(i)]
        else:
            new += i
    return new

def randomkey():
    l=list[listw]
    random.shuffle(l)
    return ''.join(l)


if key == 'y':
    print('your key :', randomkey())
    key = randomkey()

if validkey():
    if ops == 'e':
        print('encrypted text :',translate(listw, key))

    elif ops == 'd':
        print('decrypted text :',translate(key, listw))

else:
    print('please enter a valid key.....')
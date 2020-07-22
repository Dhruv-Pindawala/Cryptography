letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

msg = input('enter the text : ').upper

key = input('enter the key : ').upper()

ops = input('what do you want to do, enter e to encrypt and d to decrypt : ')


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

if ops == 'e' or ops == 'd' :
    print('encrypted text :',translate(key, msg, ops))

else:
    print('enter a valid ops......')
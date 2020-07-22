key=int(input('what is the key : '))

message=input('what do you want to share : ')

ops=input('what do you want to do, press e to encrypt and d to decrypt : ')

capital='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small='abcdefghijklmnopqrstuvwxyz'
new=''

if ops == 'e':
    for alpha in message:
        if alpha.isupper():
            n=(capital.index(alpha)+key)%26
            new+=capital[n]
        elif alpha.islower():
            n=(small.index(alpha)+key)%26
            new+=small[n]
        else:
            new+=alpha
    print(new)

elif ops=='d':
    for alpha in message:
        if alpha.isupper():
            n=(capital.find(alpha)-key)%26
            new+=capital[n]
        elif alpha.islower():
            n=(small.find(alpha)-key)%26
            new+=capital[n]
        else:
            new+=alpha
    print(new)

else:
    print('enter a valid ops')
    
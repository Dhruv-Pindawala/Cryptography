message=input('enter the text = ').lower() #to avoid hassel as all we doing is trying to get the key orr the message
listw='abcdefghijklmnopqrstuvwxyz'

for i in range(1,27):
    new = ''
    for j in message:
        if j in listw:
            n=(listw.index(j)-i)%26
            new+=listw[n]
        else:
            new+=j
    print('key =',i,"message is =",new)

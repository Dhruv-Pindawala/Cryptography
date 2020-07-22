import numpy as np
import math

key=int(input('enter the key = '))

msg=input('enter your message = ')

ops = input('what do you want to do, enter e to encrypt, d to decrypt = ')

l=len(msg)

rows=math.ceil(l/key)

if ops=='e':
    block = np.full((rows,key),'01')
    n=0
    
    for i in range(rows):
        for j in range(key):
            if n<l:
                block[i][j]=msg[n]
                n+=1
    
    new=''
    
    for j in range(key):
        for i in range(rows):
            if block[i][j]!='01':
                new+=block[i][j]
    
    print('the cipher text is :',new+'|')#| is added at the end to mark the ending of the cipher-text

elif ops=='d':
    block = np.full((key,rows),'01')
    
    left=key*rows - l
    r=key-1
    
    while left>0:
        block[r][rows-1]='02'
        r-=1
        left-=1
    
    n=0
    
    for i in range(key):
        for j in range(rows):
            if n<l and block[i][j]!='02':
                block[i][j]=msg[n]
                n+=1
    new=''
    
    for j in range(rows):
        for i in range(key):
            if block[i][j]!='02':
                new+=block[i][j]
    
    print('the plaintext is :', new)

else:
    print('please enter a vaild ops')

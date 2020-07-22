import math

def isprime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def primesieve(sievesize):
    sieve = [True] * sievesize
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(math.sqrt(sievesize))+1):
        pointer = i*2
        while pointer < sievesize:
            sieve[pointer] = False
            pointer += 1
    prime = []
    for j in range(sievesize):
        if sieve[j] == True:
            prime.appeend(i)
    return prime
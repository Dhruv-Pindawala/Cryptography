import random, sys, os, rabinmiller, cryptomath
user = input('eenter the name of the user whose files you want to create : ')

def main(name):
    print('Generating key files....')
    keyfiles(name, 1024)
    print('Key files generated.')

def generatekey(keysize):
    print('Generating p prime....')
    p = rabinmiller.generateprime(keysize)
    print('Generating q prime....')
    q = rabinmiller.generateprime(keysize)
    n = p*q
    print('Generating e which is relatively prime to (p-1)*(q-1)')
    while True:
        e = random.randrange(2**(keysize-1), 2**keysize)
        if cryptomath.gcd(e, (p-1)*(q-1)) == 1:
            break
    print('Calculating d which is mod inverse of e....')
    d = cryptomath.modinv(e, (p-1)*(q-1))
    publickey = (n, e)
    privatekey = (n, d)
    print('Public key :', publickey)
    print('Private key :', privatekey)
    return (publickey, privatekey)

def keyfiles(name, keysize):
    if os.path.exists('%s_pubkey.txt'%name) or os.path.exists('%s_privkey.txt'%name):
        sys.exit('Warning: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.' % (name, name))
    publickey, privatekey = generatekey(keysize)
    print('Creating a file for public key by the name %s_pubkey.txt'%name)
    fo = open('%s_pubkey.txt'%name, 'w')
    fo.write('%s,%s,%s' % (keySize, publicKey[0], publicKey[1]))
    fo.close()
    print('Creating a file for private key by the name %s_privkey.txt'%name)
    fo = open('%s_privkey.txt', 'w')
    fo.write('%s,%s,%s' % (keysize, privatekey[0],privatekey[1]))
    foo.close()

if __name__ == '__main__':
    main(user)
import sys
defblocksize = 128 #128 bytes
bytesize = 256 # one byte has 256 different values
name = input('enter the name wsing which files were created : ')
ops = input('what do you want to do, enter e to encrypt and d to decrypt : ')
def main(mode):
    filename = 'encrypted_file.txt'
    if mode == 'e':
        text = input('Please enter your text : ')
        pubkey = '%s_pubkey.txt'%name
        print('Encrypted text :')
        print(encrypt(filename, pubkey, msg))
    elif mode == 'd':
        privkey = '%s_privkey.txt'%name
        print('Decrypted text :')
        print(decrypt(filename, privkey))
    else:
        print('Please enter a correct operation, it is case sensitive.')

def blockfromtext(msg, blocksize = defblocksize):
    msgbytes = msg.encode('ascii')
    blockints = []
    for blockstart in range(0, len(msgbytes), blocksize):
        blockint = 0
        for i in range(blockstart, min(blockstart+blocksize, len(msgbytes))):
            blockint += msgbytes[i]*(bytesize**(i%blocksize))
        blockints.append(blockint)
    return blockints

def textfromblocks(blockints, msglen, blocksize = defblocksize):
    msg = []
    for blockint in blockints:
        blockmsg = []
        for i in range(blocksize-1, -1, -1):
            if len(msg) + i < msglen:
                asciinum = blockint // (bytesize**i)
                blockint %= (bytesize**i)
                blockmsg.insert(0, chr(asciinum))
        msg.extend(blockmsg)
    return ''.join(msg)

def encryptmsg(msg, key, blocksize = defblocksize):
    encryptedblocks = []
    n, e = key
    for block in blockfromtext(msg, blocksize):
        encryptedblocks.append(pow(block, e, n))
    return encryptedblocks

def decryptmsg(encryptedblocks, msglen, key, blocksize = defblocksize):
    decryptedblocks = []
    n, d = key
    for block in encryptedblocks:
        decryptedblocks.append(pow(block, d, n))
    return textfromblocks(decryptedblocks, msglen, blocksize)

def readkeyfile(keyfilename):
    fo = open(keyfilename)
    content = fo.read()
    fo.close()
    keysize, n, eord = content.split(',')
    return (int(keysize), int(n), int(eord))

def encrypt(msgfile, keyfile, msg, blocksize = defblocksize):
    keysize, n, e = readkeyfile(keyfile)
    if keysize < blocksize*8:
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size. Either increase the block size or use different keys.' % (blockSize * 8, keySize))

    encryptedblocks= encryptmsg(msg, (n, e), blocksize)

    for i in range(len(encryptedblocks)):
        encryptedblocks[i] = str(encryptedblocks[i])
    encryptedcontent = ','.join(encryptedblocks)
    encryptedcontent = '%s_%s_%s'%(len(msg), blocksize, encryptedcontent)
    fo = open(msgfile, 'w')
    fo.write(encryptedcontent)
    fo.close()
    return encryptedcontent

def decrypt(msgfile, keyfile):
    keysize, n, d = readkeyfile(keyfile)
    fo = open(msgfile)
    content = fo.read()
    msglen, blocksize, encryptedmsg = content.split('_')
    msglen = int(msglen)
    blocksize = int(blocksize)

    if keysize < blocksize*8:
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or lessthan the key size. Did you specify the correct key file and encrypted file?' % (blockSize * 8, keySize))
    encryptedblocks = []
    for block in encryptedmsg.split(','):
        encryptedblocks.append(int(block))
    
    return decryptmsg(encryptedblocks, msglen, (n, d), blocksize)

if __name__ = '__main__':
    main(ops)
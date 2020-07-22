import pprint

def wordpattern(word):
    word = word.upper()
    next = 0
    letternum = {}
    pattern = []
    for i in word:
        if i not in letternum:
            letternum[i] = str(next)
            next += 1
        pattern.append(letternum[i])
    return '.'.join(pattern)

def main1():
    patterns = {}

    file1 = open('hack simple sub cipher\dictionary.txt')
    wordlist = file1.read().split('\n')
    file1.close()

    for j in wordlist:
        p = wordpattern(j)

        if p not in patterns:
            patterns[p] = [j]
        else:
            patterns[p].append(j)
    
    file2 = open('hack simple sub cipher\wordpatterns.py', 'w')
    file2.write('patterns = ')
    file2.write(pprint.pformat(patterns))
    file2.close()

if __name__ == '__main__':
    main1()
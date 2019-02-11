# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 17:09:40 2018

@author: liebe
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 21:09:05 2018

@author: prem chand avanigadda
"""
import numpy as np
#constant global variables
FREQ_ALPHABETS = ['E','T','A','O','I','N','S','H','R']
DIGRAMS = ['TH','HE','IN','ER','AN','RE','ED','ON','ES','ST','EN','AT','TO','NT','HA','ND','OU','EA','NG','AS','OR','TI','IS','ET','IT','AR','TE','SE','HI','OF']
TRIGRAMS = ['THE','ING','AND','HER','ERE','ENT','THA','NTH','WAS','ETH','FOR','DTH']
ALPHABETS = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
def Gcd(a,b):
    while(b):
        a,b = b,a%b
    return a

def cleanCipher(cipher):
    return ''.join(a for a in cipher if a.isalnum() and not a.isdigit())

def readFile():
    filename = raw_input("Enter cipher file name to decrypt:")
    with open(filename,'r') as cipherfile:
        ciphertext = cipherfile.read().replace('\n','')
    return ciphertext

def alphaValue(key):
    return ALPHABETS.get(key)

def alphaChar(v):
    for key,val in ALPHABETS.items():
        if v==val:
            return key
    return 1

def alphabetFreq(cipher):
    alphacount = {}
    totalwords = 0
    for char in cipher:
        if char in alphacount:
            totalwords += 1
            alphacount[char] += 1
        else:
            totalwords += 1
            alphacount[char] = 1
    list1=sorted(alphacount, key=alphacount.get)
    list1.reverse()
    return list1

def diFreq(cipher,commonChar):
    alphacount = {}
    for char in cipher:
        if commonChar in char:
            if char in alphacount:
                alphacount[char] += 1
            else:
                alphacount[char] = 1
    list1=sorted(alphacount, key=alphacount.get)
    list1.reverse()
    return list1

def digram(cipher):
    return [cipher[i:i+2] for i in range(0,len(cipher),1)]

def trigram(cipher):
    return [cipher[i:i+3] for i in range(0,len(cipher),1)]

def modInverse(x):
    x = x%26
    for i in range(1,26):
        if((x*i)%26==1):
            return i
    return 1

def nGcd(nlist):
    print nlist
    m = Gcd(nlist[0],nlist[1])
    for i in range(2,len(nlist)):
        m=Gcd(m,nlist[i])
    return m

def filterFreq(list1,m):
    m=list(m)[0]
    list2=[]
    for char in list1:
        if char.endswith(m):
            list2.append(char)
    return list2
def detMatrix(mat1):
    return (mat1.item(0)*mat1.item(3))-(mat1.item(1)*mat1.item(2))
def matrixModulo(mat):
    for i,j in [(x, y) for x, y in np.ndindex(mat.shape)]:
        mat[i,j]=mat[i,j]%26
    return mat
def matrixInverse(mat1):
    det = detMatrix(mat1)
    detI = modInverse(det)
    adj = np.matrix([[mat1.item(3),-mat1.item(1)],[-mat1.item(2),mat1.item(0)]])
    matI=detI*adj
    return matrixModulo(matI)
def slovePuzzle(cipher1,cipher2):
    plain1=list("TH")
    plain2=list("ST")
    plain1=[alphaValue(i) for i in plain1]
    plain2=[alphaValue(i) for i in plain2]
    cipher1=[alphaValue(i) for i in cipher1]
    cipher2=[alphaValue(i) for i in cipher2]
    mat1=np.matrix([plain1,plain2])
    mat2=np.matrix([cipher1,cipher2])
    mat1I=matrixInverse(mat1)
    key = mat1I * mat2
    return matrixModulo(key)

def decrypt(cipher,ciphersplit,key):
    plaintext=""
    keyI=matrixInverse(key)
    print keyI
    for char in ciphersplit:
        y = np.matrix([alphaValue(i) for i in list(char)])
        x = y * keyI
        x = np.array(matrixModulo(x))
        x = [alphaChar(i) for i in x[0]]
        for w in x:
            plaintext=plaintext+w
    return plaintext+"\n"
def hillDecryption(cipher,freq):
    f = open("hilltextplain.txt", "a")
    cipherSplit = [cipher[i:i+2] for i in range(0,len(cipher),2)]
    list1= alphabetFreq(cipherSplit)
    for l in range(0,len(list1),1):
        cipher1 = list1[l]
        for m in range(0,len(list1),1):
            cipher2=list1[m]
            key=slovePuzzle(cipher1,cipher2)
            if(Gcd(abs(detMatrix(key)),26)==1):
                print key
                print cipher1,cipher2
                x=decrypt(cipher,cipherSplit,key).lower()
                print x
                f.write(x+"\n")
        break
if __name__ == "__main__":
    ciphertext=cleanCipher(readFile())
    freq=alphabetFreq(ciphertext)
    hillDecryption(ciphertext,freq)


    
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 20:44:20 2018

@author: prem chand Avanigadda
Course: CSCI55500
IUPUI
"""
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

def modInverse(x):
    x = x%26
    for i in range(1,26):
        if((x*i)%26==1):
            return i
    return 1

def sloveEquation(m,n,x,y):
    #ma+b=x
    #na+b=y
    m,n,x,y=alphaValue(m),alphaValue(n),alphaValue(x),alphaValue(y)
    val1=0
    val2=0
    a=0
    b=0
    if(m>n):
        val1=modInverse(m-n)
        val2=x-y
    else:
        val1=modInverse(n-m)
        val2=y-x
    a=(val1*val2)%26
    b=(x-(m*a))%26
    return a,b

def affineDecryption(cipher,freq):
    plaintext=""
    for i in range(0,len(FREQ_ALPHABETS)-1,1):
        for j in range(0,len(freq)-1,1):
            m=FREQ_ALPHABETS[0]
            n=FREQ_ALPHABETS[i+1]
            x=freq[0]
            y=freq[j+1]
            a,b=sloveEquation(m,n,x,y)
            if(Gcd(a,26)==1):
                print a,b
                for w in cipher:
                    cVal = alphaValue(w)
                    rVal = (modInverse(a)*(cVal-b))%26
                    plaintext+=alphaChar(rVal)
                plaintext+="\n\n"
            break
        plaintext+="\n"
    return plaintext

if __name__ == "__main__":
    ciphertext=cleanCipher(readFile())
    freq=alphabetFreq(ciphertext)
    plaintext=affineDecryption(ciphertext,freq)
    print plaintext.lower()
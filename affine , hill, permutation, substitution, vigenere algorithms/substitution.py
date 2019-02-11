# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 18:44:07 2018

# -*- coding: utf-8 -*-

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

def qudgram(cipher):
    return [cipher[i:i+4] for i in range(0,len(cipher),4)]

def askInput(alphabets):
    for k,v in alphabets.iteritems():
        if(v==0):
            dummy = raw_input("suggest char of"+str(k)+":")
            if(dummy):
                alphabets[k]=dummy
    return alphabets
def subsCipher(cipherclean,cipher,freq):
    alphabets = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
    di=digram(cipherclean)
    tri=trigram(cipherclean)
    quad = qudgram(cipherclean)
    commonChar = freq[0]
    freDigrams=diFreq(di,commonChar)
    freTrigrams=diFreq(tri,commonChar)
    frequad=diFreq(quad,commonChar)
    print freq
    print alphabetFreq(di)
    print alphabetFreq(tri)
    print alphabetFreq(quad)
    print freDigrams
    print freTrigrams
    print frequad
    obj = cipherText(cipher,alphabets)
    while(True):
        alphabets=askInput(alphabets)
        obj.alphabets=alphabets
        obj.decryptor()
        loop=raw_input("key board intrept to stop:")
        if(loop):
            break

class cipherText:
    alphabets=None
    cipher=None
    def __init__(self,cipher1,alpha):
        self.cipher = cipher1
        self.alphabets = alpha
    def decryptor(self):
        print self.alphabets
        for k,v in self.alphabets.iteritems():
            if(v!=0):
                self.cipher=self.cipher.replace(k,v)
        print self.cipher

if __name__ == "__main__":
    ciphertext=readFile()
    cipherclean=cleanCipher(ciphertext)
    freq=alphabetFreq(cipherclean)
    subsCipher(cipherclean,ciphertext,freq)
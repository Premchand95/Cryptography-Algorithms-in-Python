# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 12:01:46 2018

@author: prem chand Avanigadda
Course: CSCI55500
IUPUI
"""

from itertools import permutations
import numpy as np
#constant global variables
FREQ_ALPHABETS = ['E','T','A','O','I','N','S','H','R']
DIGRAMS = ['TH','HE','IN','ER','AN','RE','ED','ON','ES','ST','EN','AT','TO','NT','HA','ND','OU','EA','NG','AS','OR','TI','IS','ET','IT','AR','TE','SE','HI','OF']
TRIGRAMS = ['THE','ING','AND','HER','ERE','ENT','THA','NTH','WAS','ETH','FOR','DTH']
ALPHABETS = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}

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
def possibleSize(cipher):
    length=len(cipher)
    listLen=[]
    for i in range(2,11,1):
        if(length%i==0):
            listLen.append(i)
    return listLen

def decryptor(key,cipherSplit):
    f = open("permutationresult2.txt", "a")
    plantext=''
    for cipherword in cipherSplit:
        for n in key:
            plantext += cipherword[n]
    #filter\
    if(plantext[:3]=="THE"):
        f.write(plantext.lower()+"\n\n\n")

def writePlain(list1,word,cipherSplit):
    if(len(list1)>0):
        for plain in list1:
            key=[]
            for letter in plain:
                key.append(word.index(letter))
            decryptor(key,cipherSplit)


def findTHE1(list1,cipherSplit):
    word=cipherSplit[0]
    list2=[]
    combinations = [''.join(p) for p in permutations(list(word))]
    combinations = list(set(combinations))
    for m in combinations:
        list2.append(''.join(m))
    writePlain(list2,word,cipherSplit)

def permutationDecryption1(cipher,freq):
    print cipher
    for m in range(1,11,1):
        try:
            if(m>1):
                cipherSplit = [cipher[i:i+m] for i in range(0,len(cipher),m)]
                print cipherSplit
                findTHE1(cipherSplit,cipherSplit)
        except:
            continue 
if __name__ == "__main__":
    ciphertext=cleanCipher(readFile())
    freq=alphabetFreq(ciphertext)
    print ciphertext
    print "\n"
    permutationDecryption1(ciphertext,freq)

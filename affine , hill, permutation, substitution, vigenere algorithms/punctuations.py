# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 19:20:09 2018

@author: liebe
"""

def cleanCipher(cipher):
    pun=[]
    for i in range(0,len(cipher),1):
        if(not cipher[i].isalnum()):
            pun.append([cipher[i],i])
    return pun,len(cipher)

def readFile():
    filename = raw_input("Enter cipher file name to decrypt:")
    with open(filename,'r') as cipherfile:
        ciphertext = cipherfile.read()
    return ciphertext

def putPun(res,pun,l):
    for i in range(0,len(pun),1):
        char=pun[i][0]
        index=int(pun[i][1])
        res=res[:index] +char+ res[index:]
    print res
if __name__ == "__main__":
    pun,l=cleanCipher(readFile())
    res=raw_input("enter result: ")
    result = putPun(res,pun,l)
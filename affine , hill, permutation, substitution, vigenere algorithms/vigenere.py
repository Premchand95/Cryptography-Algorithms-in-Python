# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 21:09:05 2018

@author: prem chand avanigadda
"""
#constant global variables
ALPHABETS = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
alphaBets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
englishFreq = [.082,.015,.028,.043,.127,.022,.020,.061,.070,.002,.008,.040,.024,.067,.075,.019,.001,.060,.063,.091,.028,.010,.023,.001,.020,.001];
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
def trigram(cipher):
    return [cipher[i:i+3] for i in range(0,len(cipher),1)]

def nGcd(nlist):
    m = Gcd(nlist[0],nlist[1])
    for i in range(2,len(nlist)):
        m=Gcd(m,nlist[i])
    return m

def freqAlpha(cipher):
    f=range(len(alphaBets))
    for i in range(len(alphaBets)):
        f[i] = cipher.count(alphaBets[i]);
    return f

def IC(string1):
    len1=float(len(string1))
    f=freqAlpha(string1)
    val=0.0
    for v in f:
        val=val+(v*(v-1))
    denom = len1*(len1-1)
    return val/denom
    
def findM(substrings,m):
    if(m>1):
        list1=[]
        for i in range(0,m,1):
            dummy=''
            for word in substrings:
                try:
                    dummy=dummy+word[i]
                except:
                    continue
            list1.append(dummy)
        list2 = [IC(word) for word in list1]
        return sum(list2)/float(len(list2))
def kasiskiTest(cipher):
    tri = trigram(cipher)
    possibleLen=[]
    for word in tri:
        try:
            dist = []
            for i in range(0,len(cipher),1):
                if cipher[i:i+3]==word:
                    dist.append(int(i))
            possibleLen.append(nGcd(dist[1:]))
        except:
            continue
    return list(set(possibleLen))
def findMg(stringY):
    MgList=[]
    n=len(stringY)
    freq=freqAlpha(stringY)
    for j in range(0,26,1):
        mg=0.0
        for i in range(0,26,1):
            dummy=(i+j)%26
            mg += ((englishFreq[i]*freq[dummy]) / float(n));
        MgList.append(mg)
    return MgList
    
            
def decryptor(key,substrings):
    plaintext=''
    for word in substrings:
        for i in range(0,len(key),1):
            try:
                plaintext += alphaChar((alphaValue(word[i])-key[i])%26).lower()
            except:
                continue
    print plaintext

def vigenereDecryption(cipher):
    mList=kasiskiTest(ciphertext)
    posskeys=[]
    for m in mList:
        substrings = [cipher[i:i+m] for i in range(0,len(cipher),m)]
        resM=findM(substrings,m)
        if(0.06<resM<0.069):
            posskeys.append(m)
    for m in posskeys:
        print m
        key=[]
        substrings = [cipher[i:i+m] for i in range(0,len(cipher),m)]
        list1=[]
        for i in range(0,m,1):
            dummy=''
            for word in substrings:
                try:
                    dummy=dummy+word[i]
                except:
                    continue
            list1.append(dummy)
        for i in range(0,m,1):
            MgList=findMg(list1[i])
            key.append(MgList.index(max(MgList)))
        print key
        decryptor(key,substrings)
        break

if __name__ == "__main__":
    ciphertext=cleanCipher(readFile())
    vigenereDecryption(ciphertext)
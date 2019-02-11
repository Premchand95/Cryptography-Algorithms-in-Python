# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 18:45:11 2018

@author: liebe
"""
from sympy import mod_inverse,nextprime

mat = [[' ','!',  '"', '#', '$',  '%', '&', "'", '(', ')'], 
['*', '+', ',', '-', '.', '/', '0',  '1',  '2', '3'],
 ['4', '5',' 6', '7' ,'8', '9', ':', ';','<','='],
['>','?','@', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'],
['R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','['],
['\\',']','^','_','`','a', 'b', 'c', 'd', 'e'],
['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' ,'n', 'q'],
['o', 'p', 'v', 'r', 's', 't', 'u', 'x', 'w', '{'],
['|','y', 'z', '}', '~',' ',' ','\n','\r',' ']]
def readFile(text):
    filename = input("Enter "+ text +" filename:")
    with open(filename,'r') as InputFile:
        res = InputFile.read().split("\n")
    return res
def modInverse(a,b):
    return mod_inverse(a,b)
def find_s(y,w,m):
    return (int(y)*modInverse(w,m))%m;

def find_a(b,m,w):
    a=[]
    wi = modInverse(w,m)
    for val in b:
        a.append((int(val)*wi)%m)
    return a

def superIncressingAlgo(a,s):
    x=[]
    for i in range(len(a)-1,-1,-1):
        if s>=a[i]:
            x.append(1)
            s=s-a[i]
        else:
            x.append(0)
    return x[::-1]

def find_pi(a,b):
    pi=[]
    for val in a:
        for i in range(len(b)):
            if(val==b[i]):
                pi.append(i+1)
    return pi

def permutationPi(pi,r):
    x=[]
    for val in pi:
        x.append(r[val-1])
    return x
def intTochar(n):
    res=[str(n)[i:i+2] for i in range(0, len(str(n)), 2)]
    for val in res:
        temp=mat[int(val[1])][int(val[0])]
        #char = chr(int(temp))
        print(temp,end ="")   
def decryption(y):
    s=find_s(y,w,m)
    r=superIncressingAlgo(a_sort,s)
    x=permutationPi(pi,r)
    x=map(str,x)
    res=str(int(''.join(x),2))
    if(len(res)<14):
        l=14-len(res)
        str1 = "0"*l
        res=str1+res
    return res

if __name__ == "__main__":
    m=nextprime(2036764117802210446778721319780021001)
    w = nextprime(127552671440279916013001)
    #m=2036764117802210446778721319780021357
    #w=127552671440279916013021
    y=readFile("y")
    b=readFile("knapsack")
    a=find_a(b,m,w)
    a_sort = sorted(a)
    pi=find_pi(a,a_sort)
    res=[]
    for val in y:
        res.append(decryption(val))
    for r in res:
        intTochar(r)

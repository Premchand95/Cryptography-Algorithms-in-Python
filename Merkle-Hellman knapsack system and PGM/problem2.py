# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:08:59 2018

@author: liebe
"""
from sympy.combinatorics import Permutation

mat = [' ','!',  '"', '#', '$',  '%', '&', "'", '(', ')','*', '+', ',', '-', '.', '/', '0',  '1',  '2', '3','4', '5','6', '7' ,'8', '9', ':', ';','<','=','>','?','@', 'A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','[','\\',']','^','_','`','a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' ,'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','{', '|', '}', '~','\n','\r']

def readlogFile():
    filename = input("Enter the PGM log filename:")
    alpha=[]
    beta=[]
    with open(filename,'r') as InputFile:
        res = InputFile.read().split("\n")
        for i in res:
            temp=[int(x) for x in i.split()]
            alpha.append(temp[:10])
            beta.append(temp[10:])
    return alpha,beta

def find_r(alpha,beta):
    r=[]
    p=[]
    a,b=[],[]
    lr=len(alpha[0])
    lc=len(alpha)
    while(lc!=0):
        p.append([i for i in range(lr)])
        r.append(lr)
        a.append(alpha[:lr])
        alpha=alpha[lr:]
        b.append(beta[:lr])
        beta = beta[lr:]
        lc=lc-lr
        lr=lr-1
    return r,p,a,b
def find_m(r):
    m=[1]
    for i in range(len(r)):
        m.append(m[i]*r[i])
    return m

def find_pm(m,p):
    pm=[]
    for i in range(len(m)-1):
        pm.append([m[i]*x for x in p[i]])
    return pm

def find_alpha_indx(seed,pm):
    alphavals = [None for i in range(len(pm))]
    for i in range(len(pm)-1,-1,-1):
        for j in range(len(pm[i])-1,-1,-1):
            if(seed>=pm[i][j]):
                seed = seed-pm[i][j]
                if(alphavals[i]==None):
                    alphavals[i]=j
    return alphavals
def find_alpha_val(alphaInd,alpha):
    alphaval=[]
    for i in range(len(alphaInd)):
        alphaval.append((alpha[i][alphaInd[i]]))
    return alphaval

def find_alphaCap(alphaVal):
    l1 = Permutation([x-1 for x in alphaVal[0]])
    l2 = Permutation([x-1 for x in alphaVal[1]])
    l3 = Permutation([x-1 for x in alphaVal[2]])
    l4 = Permutation([x-1 for x in alphaVal[3]])
    l5 = Permutation([x-1 for x in alphaVal[4]])
    l6 = Permutation([x-1 for x in alphaVal[5]])
    l7 = Permutation([x-1 for x in alphaVal[6]])
    l8 = Permutation([x-1 for x in alphaVal[7]])
    return [x+1 for x in list(l8*l7*l6*l5*l4*l3*l2*l1)]

def find_betaTemp(alphaCap,temp,n):
    for j in range(len(temp)):
        if(temp[j][n]==alphaCap[n]):
            return temp[j],j

def Inverse(a):
    l1 = [x-1 for x in a]
    l=[None for x in a]
    for i in range(len(a)):
        l[l1[i]]=i
    return [x+1 for x in l]

def find_betaCap(alpha1,beta,n):
    bt,b=find_betaTemp(alpha1,beta[n],n)
    btI = Inverse(bt)
    alpha2 = [x+1 for x in list(Permutation([x-1 for x in alpha1])*Permutation([x-1 for x in btI]))]
    return alpha2,b

def betaFinal(alphaCap,beta):
    alphatemp=alphaCap
    b=[]
    for i in range(len(beta)):
        alphatemp,a=find_betaCap(alphatemp,beta,i)
        b.append(a)
    return b
def find_vals(betaCap,pm):
    l=[]
    for i in range(len(betaCap)):
        l.append(pm[i][betaCap[i]])
    return l
def readCipherFile():
    filename = input("Enter the cipher filename:")
    finalres=''
    with open(filename,'r') as InputFile:
        res = InputFile.read().split("\n")
        for i in res:
            finalres = finalres+i
    return [finalres[j:j+3] for j in range(0, len(finalres), 3)]

def decryption(pm,alpha,beta,y,seed):
    alphaInd = find_alpha_indx(seed,pm)
    alphaVal = find_alpha_val(alphaInd,alpha)
    alphaCap = find_alphaCap(alphaVal)
    betaCap = betaFinal(alphaCap,beta)
    des = find_vals(betaCap,pm)
    xVal=abs((y-sum(des))%(95)**3)
    xChar= mat[xVal//95**2]
    xVal=xVal%95**2
    yChar = mat[xVal//95]
    zChar = mat[xVal%95]
    return xChar+yChar+zChar
def getcipherVal(val):
    x,y,z=mat.index(val[0]),mat.index(val[1]),mat.index(val[2])
    val = x*95*95+y*95+z
    return val
if __name__ == "__main__":
    a,b = readlogFile()
    r,p,alpha,beta=find_r(a,b)
    m=find_m(r)
    pm = find_pm(m,p)
    cipher = readCipherFile()
    seed = int(input("enter seed :"))
    finalres=""
    for val in cipher:
        y = getcipherVal(val)
        x=decryption(pm,alpha,beta,y,seed)
        seed = seed+1
        finalres=finalres+x
    print(finalres)
    
    
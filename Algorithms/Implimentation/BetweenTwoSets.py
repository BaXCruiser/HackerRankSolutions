# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:50:16 2019

@author: BaX Cruiser
"""

def getTotalX(a, b):
    nmax,nmin,count = max(a),min(b),0
    for i in range(1,int(nmin/nmax)+1):
        if(sum((i*nmax)%n for n in a)+sum(n%(i*nmax) for n in b))==0:
            count+=1
    return count

if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    print(getTotalX(a, b))
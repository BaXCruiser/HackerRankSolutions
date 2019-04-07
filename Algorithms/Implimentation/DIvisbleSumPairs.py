# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:15:49 2019

@author: BaX Cruiser
"""


def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(0,n-1):
        for j in range (i+1,n):
            if not (ar[i]+ar[j])%k:
                count+=1
    return count

if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    ar = list(map(int, input().rstrip().split()))
    print(divisibleSumPairs(n, k, ar))

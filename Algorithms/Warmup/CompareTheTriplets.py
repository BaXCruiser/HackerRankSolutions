# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:58:43 2019

@author: BaX Cruiser
"""

def compareTriplets(a, b):
    aScore=0
    bScore=0
    for i in range(3):
        if a[i]>b[i]:
            aScore+=1
        if b[i]>a[i]:
            bScore+=1
    return aScore,bScore

if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    print(result[0],result[1])

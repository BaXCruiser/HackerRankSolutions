# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:11:07 2019

@author: BaX Cruiser
"""
def diagonalDifference(arr,n):
    d1=0
    d2=0
    for i in range (0,n):
        for j in range (0,n):
            if i==j:
                d1+=arr[i][j]
            if i+j==n-1:
                d2+=arr[i][j]
    return abs(d1-d2)

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr,n)
    print(result)

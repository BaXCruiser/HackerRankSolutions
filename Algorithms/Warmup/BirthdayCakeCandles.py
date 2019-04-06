# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:52:33 2019

@author: BaX Cruiser
"""
def birthdayCakeCandles(ar):
    return ar.count(max(ar))

if __name__ == '__main__':
    n= int(input())
    ar=list(map(int, input().rstrip().split()))
    print(birthdayCakeCandles(ar))

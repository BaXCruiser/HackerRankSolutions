# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:48:17 2019

@author: BaX Cruiser
"""

def simpleArraySum(ar):
    return sum(ar)

if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    print(simpleArraySum(ar))

# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:06:20 2019

@author: BaX Cruiser
"""
def birthday(s, d, m):
    ways=0
    for i in range(0,len(s)-m+1):
        su=0
        for j in range(i,i+m):
            su+=s[j]
        if su==d:
            ways+=1
    return ways

if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().rstrip().split()
    d = int(dm[0])
    m = int(dm[1])
    print(birthday(s, d, m))
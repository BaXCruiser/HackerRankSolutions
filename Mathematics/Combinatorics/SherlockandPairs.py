#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:51:04 2020

@author: baxcruiser
"""


def solve(a):
    count=0
    m={}
    for e in a:
        if e not in m:
            m[e]=1
        else: 
            m[e]+=1
    for e in m.values():
        if e !=1:
            count+=e*(e-1)
    return count
    

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        a_count = int(input())
        a = list(map(int, input().rstrip().split()))
        print(solve(a))

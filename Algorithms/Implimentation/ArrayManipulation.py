#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 23:14:37 2020

@author: baxcruiser
"""

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    l=[0 for i in range(n)]
    t=0
    for q in queries:
        l[q[0]-1]+=q[2]
        if q[1]<n:
            l[q[1]]-=q[2]
    max=t
    for e in l:
        t+=e
        if(max<t):
            max=t
    return max


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print (result)
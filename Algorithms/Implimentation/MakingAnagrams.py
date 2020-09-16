#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 01:07:37 2020

@author: baxcruiser
"""


import os

def makeAnagram(a, b):
    n=0
    s=set(a).intersection(set(b))
    for e in s:
        n+=min(a.count(e),b.count(e))
    return (len(a)+len(b)-n*2)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

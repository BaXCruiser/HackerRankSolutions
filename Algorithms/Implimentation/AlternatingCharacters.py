#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 01:08:30 2020

@author: baxcruiser
"""

import os

def alternatingCharacters(s):
    c=0
    for i in range (0,len(s)-1):
        if (s[i]==s[i+1]):
            c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()


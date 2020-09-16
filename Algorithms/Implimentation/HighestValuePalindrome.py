#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:09:46 2020

@author: baxcruiser
"""
#passes 28/33 test cases

#!/bin/python3

def highestValuePalindrome(s, n, k):
    l=[]
    l2=[]
    if (k>=n):
        return '9'*n
    if(len(s)==1):
        if k==1:
            return '9'
        else:
            return s
    if len(s)%2==0:
        s1=list(s[:len(s)//2])
        s2=list(s[len(s)//2:][::-1])
        m=''
    else:
        s1=list(s[:len(s)//2])
        s2=list(s[(len(s)//2)+1:][::-1])
        m=s[len(s)//2]
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            if(k==0):
                return '-1'
            s1[i]=max(s1[i],s2[i])
            s2[i]=s1[i]
            if s1[i]!='9':
               l.append(i)
            k-=1
        else :
            if(s1[i]!='9'):
                l2.append(i)
    for e in l:
        if(k>0):
            s1[e]='9'
            s2[e]='9'
            k-=1

    for e in l2:
        if s1[e]!='9' and k>=2:
            s1[e]='9'
            s2[e]='9'
            k-=2
    if k==1 and m!='':
        m='9'

    return ''.join(s1)+m+''.join(s2[::-1])



if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    print(result)

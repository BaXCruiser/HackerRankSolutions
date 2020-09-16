# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:12:09 2019

@author: BaX Cruiser
"""

n=int(input())
arr=input()
jump=0
i=1
while(i<n) :
    if arr[i]==0:
        jump+=1
        if(i<len(arr)-2 and arr[i+2]=='0' and arr[i+1]=='0')):
        i+=1
    i+=1
print(jump)

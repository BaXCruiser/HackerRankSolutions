# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:12:09 2019

@author: BaX Cruiser
"""

n=int(input())
arr=input()
jump=1
i=0
while(i<n) :
    jump+=1
    if(arr[i]!='0' or (arr[i]=='0' and arr[i-2]=='0' and arr[i-1]=='0')):
        jump-=1
    i+=1
print(jump)

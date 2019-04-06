# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:24:35 2019

@author: BaX Cruiser
"""
n=int(input())
a=input().split(" ")
p=0
n=0
z=0
for e in a:
    if(int(e)>0):
        p+=1
    elif int(e)<0:
        n+=1
    else:
        z+=1
print(format(p/len(a),"0.3f"))
print(format(n/len(a),"0.3f"))
print(format(z/len(a),"0.3f"))

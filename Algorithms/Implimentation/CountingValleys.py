# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 15:08:09 2019

@author: BaX Cruiser
"""
stepcount=int(input())
steps=input()
valley=0
valley_level=0
for step in steps :
    if step=='U':
        valley_level+=1
    if step=='D':
        valley_level-=1
    if(valley_level==0 and step=='U'):
        valley+=1
print(valley)

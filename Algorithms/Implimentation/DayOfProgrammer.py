# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:54:49 2019

@author: BaX Cruiser
"""

def dayOfProgrammer(y):
    d = 13
    if (not(y%4) and (y < 1918 or y%100 or not(y%400))):
         d-=1
    if (y == 1918):
         d = 26
    return str(d)+".09."+str(y)


if __name__ == '__main__':
    year = int(input().strip())
    print(dayOfProgrammer(year))
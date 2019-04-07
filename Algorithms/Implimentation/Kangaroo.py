# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:36:15 2019

@author: BaX Cruiser
"""

def kangaroo(x1, v1, x2, v2):
    while (x1<=x2 and v1>v2):
        x1+=v1
        x2+=v2
        if(x1==x2):
            return "YES"
    return "NO"

if __name__ == '__main__':
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    print(kangaroo(x1, v1, x2, v2))
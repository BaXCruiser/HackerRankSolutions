# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 19:26:25 2019

@author: BaX Cruiser
"""
def migratoryBirds(arr):
    count = [0]*6
    for t in map(int,arr):
        count[t]+= 1
    return(count.index(max(count)))

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    print(migratoryBirds(arr))

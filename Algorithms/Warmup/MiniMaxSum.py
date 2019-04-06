# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 19:39:13 2019

@author: BaX Cruiser
"""
def miniMaxSum(arr):
    maxSum=minSum=sum(arr)-arr[0]
    for element in arr:
        if (sum(arr)-element > maxSum):
            maxSum=sum(arr)-element
        if (sum(arr)-element < minSum):
            minSum=sum(arr)-element
    print(minSum,maxSum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)

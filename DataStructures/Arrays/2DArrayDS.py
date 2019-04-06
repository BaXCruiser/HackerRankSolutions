# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:48:42 2019

@author: BaX Cruiser
"""
def hourglassSum(arr):
    maxSum=arr[0][0]+arr[2][0]+arr[0][1]+arr[1][1]+arr[2][1]+arr[0][2]+arr[2][2]
    for i in range(0,4):
        for j in range(0,4):
            maxSum=max(maxSum,arr[i][j]+arr[i+2][j]+arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1]+arr[i][j+2]+arr[i+2][j+2])
    return maxSum

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print(result)

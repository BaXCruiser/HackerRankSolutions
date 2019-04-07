# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 18:35:07 2019

@author: BaX Cruiser
"""
def breakingRecords(scores):
    maxScore=minScore=scores[0]
    pointsMax=pointsMin=0
    for e in scores:
        if e>maxScore :
            maxScore=e
            pointsMax+=1
        if e<minScore:
            minScore=e
            pointsMin+=1
    print(pointsMax,pointsMin)
if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    breakingRecords(scores)

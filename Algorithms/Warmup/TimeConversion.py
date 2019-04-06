# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 22:37:11 2019

@author: BaX Cruiser
"""
arr = input().strip()
h, m, s = map(int, arr[:-2].split(':'))
h = h % 12 + (arr[-2:].upper() == 'PM') * 12
print(('%02d:%02d:%02d') % (h, m, s))

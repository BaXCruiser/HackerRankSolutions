# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 23:39:45 2019

@author: BaX Cruiser
"""

def gradingStudents(grades):
    for element in grades:
        if element<38 or element%5<3:
            print(element)
        else:
            print(element+5-element%5)

if __name__ == '__main__':
    n = int(input())
    grades = []
    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)
    result = gradingStudents(grades)

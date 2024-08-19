# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:54:45 2024

@author: diemtrinh
"""
a=float(input("Số thứ nhất:"))
b=float(input("Số thứ hai:"))
c=float(input("Số thứ ba:"))
if a+b>c and a+c>b and b+c>a:
    print(" a,b,c là ba cạnh của tam giác")
else:
    print("a,b,c không là ba cạnh của tam giác")

    
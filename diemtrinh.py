# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:11:15 2024

@author:diemtrinh
"""
a=float(input("Số thứ nhất:"))
b=float(input("Số thứ hai:"))
c=float(input("Số thứ ba:"))
if a+b>c and a+c>b and b+c>a:
  if a==b==c: 
    print("Day la tam giac deu")
  elif a==b or a==c or b==c:
    print("Day la tam giac can")
  elif a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
    print("Day la tam giac vuong")
  else:
        print("Day la tam giac thuong")



# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:59:24 2024

@author: diemtrinh
"""
a=float(input("Hệ số a="))
b=float(input("Hệ số b="))
c=float(input("Hệ số c="))
if a==0: print ("Phương trình không phải phương trình bậc 2")
delta= 2**b-4*a*c
if delta < 0: print ("Phương trình vô nghiệm")
elif delta == 0: print("Phương trình có 1 nghiệm duy nhất", -b/2*a)
else:
    print ("Phương trình có hai nghiệm phân biệt")
    print ("x1 =", float((-b-sqrt(delta))/(2*a)))
    print ("x2 =", float((-b+sqrt(delt))/(2*a)))
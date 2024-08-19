# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:51:07 2024

@author:diemtrinh
"""
a=float(input("Hệ số a="))
b=float(input("Hệ số b="))
if a==0 and b==0: 
    print("Phương trình vô số nghiệm")
elif b!=0 and a==0: 
    print("Phương trình vô nghiệm")
elif a!=0:
    print(" Nghiệm của phương trình là:",-b/a)



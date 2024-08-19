# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:55:22 2024

@author: diemtrinh
"""
s = float(input("Quảng đường đã đi: "))
if s <= 1:
    Tổng_tiền = s * 20000
    print("Số tiền phải trả là ",Tổng_tiền)
elif s <= 3:
    Tổng_tiền = s * 13000
    print("Số tiền phải trả là ",Tổng_tiền)
elif s <= 8:
    Tổng_tiền = 3*13000 + (s - 3) * 12000 
    print("Số tiền phải trả là ",Tổng_tiền)
elif s > 8:
    Tổng_tiền = 3 * 13000 + 5 * 12000 + (s - 8) * 10000
    print("Số tiền phải trả là ",Tổng_tiền)
elif Tổng_tiền > 100000:
    Tổng_tiền = Tổng_tiền * 0.92
    print("Số tiền phải trả là ",Tổng_tiền)
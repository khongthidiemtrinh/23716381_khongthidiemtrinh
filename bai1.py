# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:25:24 2024

@author:diemtrinh
"""
GPA=float(input("Điểm trung bình GPA="))
if GPA<3.5:xep_hang= "Học lực kém "
elif 3.5<=GPA<5.0:xep_hang= "Học lực yếu"
elif 5.0<=GPA<7.0:xep_hang= "Học lực Trung bình"
elif 7.0<=GPA<8.0:xep_hang= "Hoc lực Khá"
elif 8.0<=GPA<9.0:xep_hang= "Học lực Gioi"
elif 9.0<=GPA<=10:xep_hang= "Học lực Xuất sắc"
print("Kết quả xếp hạng học lực",xep_hang)
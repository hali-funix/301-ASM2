from itertools import count
from msilib import type_binary
import pandas as pd
import numpy as np
import re

# MON 301 - Bai tap ASM2 - HOC VIEN : LUONG DONG HAI
# SU DUNG VISUAL STUDIO CODE

filename = input("Enter a class file to grade(i.e. class1 for class1.txt): ")
filenametxt = filename + '.txt'

# Truy van truc tiep ten file
# filenametxt = 'class2.txt'

# Task 1
try:
    with open(filenametxt,'r') as file:
        print('Successfully opened ', filenametxt)
        du_lieu = file.readlines()
        
        # print(len(du_lieu))

except IOError:
    print('Can not open file')
    exit()

# Task 2
print('**** ANALYZING ****')
so_luong_dong = len(du_lieu)
so_luong_dong_loi = 0
du_lieu_hop_le = []

for tung_du_lieu in du_lieu:
    tung_du_lieu = tung_du_lieu.replace('\n', '')
    danh_sach_gia_tri = tung_du_lieu.split(',')
    id = danh_sach_gia_tri[0]
    # print(id)

    id_phan_chu = re.findall('[a-zA-Z]+', id)[0]
    # print(id_phan_chu)
    id_phan_so = re.findall('[0-9]+', id)[0]
    # print(id_phan_so)
  
    if (id_phan_chu != 'N') or (len(id_phan_so) != 8):
        print('Invalid line of data: N# is invalid')
        print(tung_du_lieu)
        so_luong_dong_loi += 1
        continue
    if (len(tung_du_lieu.split(',')) != 26):
        print('Invalid line of data: does not contain exactly 26 values:')
        print(tung_du_lieu)
        so_luong_dong_loi += 1
        
    else : 
        # print(tung_du_lieu)
        du_lieu_hop_le.append(tung_du_lieu)

print('**** REPORT ****')
print("Total valid lines of data :", so_luong_dong)
print("Total invalid lines of data: ", so_luong_dong_loi)        
# print(du_lieu_hop_le)

# Task 3
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(',')
# print(answer_key) 

hoc_vien_diem = {} 
tong_diem = []  

for diem in du_lieu_hop_le : 
    diem_hv = diem.split(',')
    cham_diem = 0
    for i, dap_so in enumerate(diem_hv[1:]):
        if dap_so == answer_key[i]: 
            cham_diem += 4
        elif dap_so != '':
            cham_diem += -1
    hoc_vien_diem [diem_hv[0]] = cham_diem
    tong_diem.append(cham_diem)

# in tong diem co MA SO HOC VIEN
# print (hoc_vien_diem)   

# in tong diem khong co MA SO HOC VIEN
# rint (tong_diem)
# print (type(tong_diem))

dem_diem_cao = sum(i >= 80 for i in tong_diem)
print ("Total student of high scores:" , dem_diem_cao)

Mean=round(np.mean(tong_diem),2)
Max=np.max(tong_diem)
Min=np.min(tong_diem)
Range=Max-Min
Median=np.median(tong_diem)

print('Mean (average) score:', Mean)
print('Highest score:', Max)
print('Lowest score:', Min)
print('Range of scores:',Range)
print('Median score:', Median)

### task 3.7 va 3.8 lam rieng 1 file py, luu cung voi thu muc nay ###


# Task4
# chuyen tu dict sang str :
hoc_vien_diem_str = str(hoc_vien_diem)
# print(hoc_vien_diem_str)
ket_qua_hv_diem = hoc_vien_diem_str.strip('{}').replace(',','\n').replace(':',',').replace("'","").replace(' ','')
# print (ket_qua_hv_diem)

luu_ket_qua = open(filename + "_grades0.txt",'w')
luu_ket_qua.write(ket_qua_hv_diem)


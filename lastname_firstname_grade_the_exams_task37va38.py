from ast import Index
from itertools import count
from msilib import type_binary
import pandas as pd
import numpy as np
import re

# MON 301 - Bai tap ASM2 - HOC VIEN : LUONG DONG HAI
# SU DUNG VISUAL STUDIO CODE

############## TASK 3.7 VA TASK 3.8 #################

filename = input("Enter a class file to grade(i.e. class2 for class2.txt): ")
filenametxt = filename + '.txt'

# Truy van truc tiep ten file
# filenametxt = 'class2.txt'

# Task 1
try:
    with open(filenametxt,'r') as file:
        print('Successfully opened ', filenametxt)
        du_lieu = file.readlines()
        # print(filenametxt)
        # print(type(du_lieu))
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
        # print('Invalid line of data: N# is invalid')
        # print(tung_du_lieu)
        so_luong_dong_loi += 1
        continue
    if (len(tung_du_lieu.split(',')) != 26):
        # print('Invalid line of data: does not contain exactly 26 values:')
        # print(tung_du_lieu)
        so_luong_dong_loi += 1
        
    else : 
        # print(tung_du_lieu)
        du_lieu_hop_le.append(tung_du_lieu)

# print('**** REPORT ****')
# print("Total valid lines of data :", so_luong_dong)
# print("Total invalid lines of data: ", so_luong_dong_loi)        
# print(du_lieu_hop_le)

# Task 3
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(',')
# print(answer_key) 
hoc_vien_diem = {} 
tong_diem = []  

###################################
# Task 3.7 va 3.8
score_3_7 = {k: 0 for k in range(1,26)}
score_3_8 = {s: 0 for s in range(1,26)}
for diem in du_lieu_hop_le : 
    diem_hv = diem.split(',')
    cham_diem = 0
    for i, dap_so in enumerate(diem_hv[1:]):
        
        if dap_so == '':
            score_3_7[i+1] += 1
        elif dap_so == answer_key[i]: 
            cham_diem += 4
        else:
            cham_diem -= 1
            score_3_8[i+1] += 1
    hoc_vien_diem [diem_hv[0]] = cham_diem
    tong_diem.append(cham_diem)
# print(score_3_7)   
# print(score_3_8)

### Task 3.7 ###
max_37 = 0

for key_37, value_37 in score_3_7.items():
		if value_37 > max_37:
			max_37 = value_37
ketqua = []
tyle_hv_boqua = round(max_37/len(du_lieu_hop_le),2)
for key_37, value_37 in score_3_7.items():
		if value_37 == max_37:
			ketqua.append(key_37)
for ketqua37 in ketqua:
	print("Question that most people skip: ", ketqua37, "-", max_37, "-",tyle_hv_boqua)

### Task 3.8 ###
max_38 = 0

for key_38, value_38 in score_3_8.items():
		if value_38 > max_38:
			max_38 = value_38
ket_qua = []
tyle_hv_sai = round(max_38/len(du_lieu_hop_le),2)
for key_38, value_38 in score_3_8.items():
		if value_38 == max_38:
			ket_qua.append(key_38)
for ketqua38 in ket_qua:
	print("Question that most people answer incorrectly: ", ketqua38, "-", max_38, "-", tyle_hv_sai)


import pandas as pd
import numpy as np

filename = input("Enter a file name: ")
data_raw = []

while True:
        try:
                with open(rf'D:\D2\FUNIX\301-GIOI THIEU DS\DSP301x_asm2_haildFX16910@funix.edu.vn\Data Files/{filename}','r') as file1:
                        print('File open successful')
                        for line in file1:
                                file_content = file1.readline().split()
                                nd = file_content[0].split(',')
                                
                                data_raw.append(nd)
                break

        except Exception:
                print('Can not open file')
                continue
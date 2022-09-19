# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 13:11:02 2021

@author: pcondon
"""

textFilePath = r"C:\Users\Padraig\Desktop\Development\AdventOfCode\P1.1\P1.txt"

file =  open(textFilePath, "r")
data = file.readlines()
data = [int(x) for x in data]

#Part 1
inc_count = 0
for i in range(1, len(data)):
    if data[i] > data[i-1]:
        inc_count +=1

print("Solution Part 1:", inc_count)    



#Part 2
inc_count = 0
for i in range(3, len(data)):
    if data[i-3] + data[i-2] + data[i-1] < data[i-2] + data[i-1] + data[i] :
        inc_count+=1

        
print("Solution Part 2:", inc_count)        
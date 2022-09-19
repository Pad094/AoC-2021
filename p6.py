# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 08:38:52 2021

@author: pcondon
"""

def ProcessDay(data):
    initialLength = len(data)
    for i in range(initialLength):
        if data[i] > 0:
            data[i]-=1
        elif data[i] ==0:
            data[i] = 6
            data.append(8)
    return data;        

def RecurseSingle(time):
  
    f0 = 1
    f1 = 0
    f2 = 0
    f3 = 0
    f4 = 0
    f5 = 0
    f6 = 0
    f7 = 0
    f8 = 0
    for i in range(time):
        f0Save = f0
        f0 = f1
        f1 = f2
        f2 = f3
        f3 = f4
        f4 = f5
        f5 = f6
        f6 = f7 + f0Save
        f7 = f8
        f8 = f0Save
    return f0 + f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8;    
        
       
file = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p6\p6.txt", 'r')
rabbits = file.readline().split(",")
rabbits = [int(x) for x in rabbits]


#Part1
rabbits_part1 = rabbits.copy()
for i in range(80):
    rabbits_part1 = ProcessDay(rabbits_part1)
    
print("Solution Part 1:", len(rabbits_part1))


#Part 2
rabbits_part2 = rabbits.copy()
totalLength = 0
for element in rabbits_part2:
    time = 256
    time -=element
    totalLength+= RecurseSingle(time)
    
    
print("Solution Part 2:", totalLength)

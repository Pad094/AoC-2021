# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 08:43:21 2021

@author: pcondon
"""

import numpy as np

def  BinToDecConvertor(val1, val2):
    val1_dec = 0
    val2_dec = 0
    
    for i in range(12):
        val1_dec += val1[i]*2**(11-i)
        val2_dec += val2[i]*2**(11-i)
    
    return val1_dec, val2_dec  


def  BinToDecConvertorStr(val1, val2):
    val1_dec = 0
    val2_dec = 0
    
    for i in range(12):
        val1_dec += int(val1[i])*2**(11-i)
        val2_dec += int(val2[i])*2**(11-i)
    
    return val1_dec, val2_dec  


def GetMostCommonBit(file, i):
       count = 0
       for j in range(len(file)):
           if int(file[j][i]) == 1:
               count = count +  1
      
       if count > len(file)/2:
           return 1
       elif count < len(file)/2:
           return 0
       else:
           return 2
       

def BuildMask(file, i, k):
    mask = []
    for j in range(len(file)):
        if int(file[j][i]) == k :
            mask.append(True)
        else:
            mask.append(False)
            
    return mask;        
                 
    


with open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\P3\P3.txt", 'r') as file:
    file = file.readlines()
    
    val1 = []
    val2 = []
    for i in range(12):
        k = GetMostCommonBit(file, i)
        if k == 1:
           val1.append(1)
           val2.append(0)
           
        else:
           val1.append(0)
           val2.append(1)
    
      
    val1_dec, val2_dec = BinToDecConvertor(val1, val2)
    print("Solution Part 1:", val1_dec*val2_dec)
    
    
    
    
    #PART 2
    #Get Oxygen:
    Oxygen = np.array(file[:])
    for i in range(12):
        k = GetMostCommonBit(Oxygen, i)
        if k == 2:
            k = 1
        Oxygen = Oxygen[BuildMask(Oxygen, i, k)]
        if len(Oxygen) ==1:
            break
        
        
      
   
    
   
    
    #Get Carbon:
    Carbon = np.array(file[:])
    for i in range(12):
        k = GetMostCommonBit(Carbon, i)
        if k == 2:
            k = 1
        Carbon = Carbon[BuildMask(Carbon, i, 1- k)]
        if len(Carbon) ==1:
            break
   
        
    #print(Carbon)      
    val1_dec, val2_dec = BinToDecConvertorStr(Oxygen[0], Carbon[0]);  
    print("Solution Part 2:", val1_dec*val2_dec)    
        
        
      
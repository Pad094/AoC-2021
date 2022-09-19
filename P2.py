# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:47:36 2021

@author: pcondon
"""

file = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\P2\P2.txt", 'r')
file = file.readlines()
file = [x.split(' ') for x in file]


#Part 1
vertical_pos = 0
horizontal_pos = 0
for i in range(len(file)):
    if file[i][0] == "up":
        vertical_pos+= int(file[i][1])
        
    elif file[i][0] == "down":
        vertical_pos-= int(file[i][1])   
     
    elif file[i][0] == "forward":
       horizontal_pos+= int(file[i][1])    
     
    elif file[i][0] == "backward":
      horizontal_pos-= int(file[i][1]) 
    
    else:
        raise Exception("Invalid entry:", file[i][0] )
        
        
print("Solution Part 1:", abs(vertical_pos*horizontal_pos))    




#Part 2    
vertical_pos = 0
horizontal_pos = 0
aim = 0
for i in range(len(file)):
    if file[i][0] == "up":
        aim-= int(file[i][1])
        
    elif file[i][0] == "down":
        aim+= int(file[i][1])   
     
    elif file[i][0] == "forward":
       horizontal_pos+= int(file[i][1])  
       vertical_pos+= int(file[i][1])*aim 

    
    else:
        raise Exception("Invalid entry:", file[i][0] )
        
        
print("Solution Part 2:", abs(vertical_pos*horizontal_pos))    
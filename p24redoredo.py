# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 15:56:11 2022

@author: Padraig
"""

import math

#Process Input
commands = []
with open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p24\p24.txt", 'r') as file:
    for line in file :
        commands.append([x for x in line.split()])       
    
instructionBlocks = []
i = 1
while i < len(commands):
    nextInstructionBlock = []
    while i < len(commands) and commands[i][0] != "inp":
        nextInstructionBlock.append(commands[i])
        i+=1
    instructionBlocks.append(nextInstructionBlock)
    i+=1
    
    
    
def ProcessInstruction(w,x,y,z, instruction):

    if instruction[1] == "w":
        val1 = w
    elif instruction[1] =="x":
        val1 = x
    elif instruction[1] =="y":
        val1 = y
    elif instruction[1] =="z":
        val1 = z  
    
    if len(instruction)>2:    
        if instruction[2] == "w":
            val2 = w
        elif instruction[2] =="x":
            val2 = x
        elif instruction[2] =="y":
            val2 = y
        elif instruction[2] =="z":
            val2 = z    
        else:
            val2 = int(instruction[2])    
    
    
    if instruction[0] == "inp":
        return int(instruction[1]), x, y, z
        
    elif instruction[0] == "add":
        #print(val1, val2)
        output = val1 + val2
            
    elif instruction[0] == "mul":
         output =val1*val2
         
    elif instruction[0] == "div":
        output = math.floor(val1/val2)
    
    elif instruction[0] == "mod":
        output = val1%val2
        
    elif instruction[0] == "eql":   
        if val1 == val2:
            output = 1
        else:
            output = 0
            
    if instruction[1] == "w":
        return output, x, y ,z
    elif instruction[1] =="x":
        return w, output, y, z
    elif instruction[1] =="y":
        return w, x, output, z
    elif instruction[1] =="z":
        return w, x, y, output 
 

def ProcessInstructionBlock(instructions, w,x,y,z):  
    for instruction in instructions:
        w,x,y,z =  ProcessInstruction(w,x,y,z, instruction)
        
    return w,x,y,z    
        
        

cache = {}
                   
def find_Optimal_start_value(commandBlocks, blockIndex, x, y, z, val, lowest):
  if (blockIndex, x, y, z) in cache:
    return cache[blockIndex, x,y, z]

  if blockIndex == len(commandBlocks):
    return val if z == 0 else 0

  numbers = range(1, 10)
  if not lowest: numbers = reversed(numbers)

  for n in numbers:
    nw, nx, ny, nz = ProcessInstructionBlock(commandBlocks[blockIndex], n, x, y, z)

    startValue = find_Optimal_start_value(commandBlocks, blockIndex + 1, nx, ny, nz, val * 10 + n, lowest)
    if startValue != 0:
      break

  cache[blockIndex, x,y, z] = startValue
  return startValue
        
model = find_Optimal_start_value(instructionBlocks, 0, 0, 0, 0, 0, False)
print(f'Biggest Valid Input: {model}')

cache = {}
model = find_Optimal_start_value(instructionBlocks, 0, 0, 0, 0, 0, True)
print(f'Smallest Valid Input: {model}')
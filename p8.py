# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 08:36:31 2021

@author: pcondon
"""
def ConvertWithCipher(cipher, element):
    element = set(element)
    codeSet = [cipher[x] for x in element]
    codeSet = set(codeSet)


    if codeSet   == {0,1,2,4,5,6}:
        return 0
    elif codeSet == {2,5}:
        return 1
    elif codeSet == {0,2,3,4,6}:
        return 2
    elif codeSet == {0,2,3,5,6}:
        return 3
    elif codeSet == {1,2,3,5}:
        return 4
    elif codeSet == {0,1,3,5,6}:
        return 5
    elif codeSet == {0,1,3,4,5,6}:
        return 6
    elif codeSet == {0,2,5}:
        return 7
    elif codeSet == {0,1,2,3,4,5,6}:
        return 8
    elif codeSet == {0,1,2,3,5,6}:
        return 9

inputFile = open(r"C:\Users\Padraig\Desktop\Development\AdventOfCode\p8\p8.txt", 'r')
inputFile = inputFile.readlines()
inputFile = [x.split("|") for x in inputFile]

outputs = [x[1] for x in inputFile]
outputs = [x.strip().split(" ") for x in outputs]

inputs = [x[0] for x in inputFile]
inputs = [x.strip().split(" ") for x in inputs]


#Part 1
n0s =0;
n1s =0;
n2s =0;
n3s =0;
n4s =0;
n5s =0;
n6s =0;
n7s =0;
n8s =0;
n9s =0;

for line in outputs:
    for element in line:
        if len(element) == 2:
            n1s+=1;
        elif len(element) == 4:
            n4s+=1;
        elif len(element) == 3:
            n7s+=1;
        elif len(element) == 7:
            n8s+=1;  
            
            
print("Solution Part 1:", n1s + n4s + n7s + n8s)            

#Part 2
totalValue = 0
for k in range(len(inputs)):
    testInput  = inputs[k]
    testOutput = outputs[k]
    
    n0s =set({"a", "b", "c", "d", "e", "f", "g"})
    n1s =set({"a", "b", "c", "d", "e", "f", "g"})
    n2s =set({"a", "b", "c", "d", "e", "f", "g"})
    n3s =set({"a", "b", "c", "d", "e", "f", "g"})
    n4s =set({"a", "b", "c", "d", "e", "f", "g"})
    n5s =set({"a", "b", "c", "d", "e", "f", "g"})
    n6s =set({"a", "b", "c", "d", "e", "f", "g"})
    
    # testInput = ["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"]
    # testOutput = ["cdfeb", "fcadb" , "cdfeb",  "cdbaf"]
    for element in testInput:
        
        #Process 1
        if len(element) == 2:
                n2s = n2s.intersection(set(element))
                n5s = n5s.intersection(set(element))    
                
                
                
         #Process 7
        if len(element) == 3:
                 n0s = n0s.intersection(set(element))
                 n2s = n2s.intersection(set(element))
                 n5s = n5s.intersection(set(element))         
                
                
                
         #Process 4
        if len(element) ==4:
             n1s = n1s.intersection(set(element))
             n2s = n2s.intersection(set(element))
             n3s = n3s.intersection(set(element))
             n5s = n5s.intersection(set(element))
             
             
         # Process 2, 3, 5
        if len(element) == 5:
             #2
             n0s = n0s.intersection(set(element))
             n3s = n3s.intersection(set(element))
             n6s = n6s.intersection(set(element))
             
             
          #Process 0, 6, 9
          
        if len(element) == 6:
              #0
              n0s = n0s.intersection(set(element))
              n1s = n1s.intersection(set(element))
              n5s = n5s.intersection(set(element))
              n6s = n6s.intersection(set(element))
              
    
    keys = [n0s, n1s, n2s, n3s, n4s, n5s, n6s] 
    
    while not all(len(element) ==1 for element in keys):
        for i in range(len(keys)):
          if len(keys[i]) ==1:
            #Remove from other lists:
                for j in range(0, i):
                    keys[j] = keys[j] - keys[i]
                    
                for j in range(i+1, len(keys)):
                    keys[j] = keys[j] - keys[i]
    #print(keys)       
             
    
    
    cipher = {}
    for i in range(len(keys)):
        iterator = iter(keys[i])
        item1 = next(iterator, None)
        cipher[item1] = i
        
    
    test = 0
    for i in range(4):
        test+= ConvertWithCipher(cipher, testOutput[i])*10**(3-i)    
        
    totalValue+= test


print("Solution Part 2:", totalValue)      
    


  
         
         
         
         
         
         
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

text_file = open ('test.txt', 'r')

list=[]
for line in text_file:
    a=line.strip()
    list.append(a)
    
print(list)
    


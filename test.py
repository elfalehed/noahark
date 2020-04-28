#! /usr/bin/env python3 # coding: UTF-8 

import os

file_count = sum(len(files) for _, _, files in os.walk(r'Prompts/challenge1/'))


for i in range(file_count)  :
    i = 1 
    pp = open ("Prompts/challenge1/p"+ str(i) +".txt","r") 
    answer = input(pp.read()) 
    if answer == "a": 
        print("Fuck ya") 

  

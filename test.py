#! /usr/bin/env python3 # coding: UTF-8 

import os

file_count = sum(len(files) for _, _, files in os.walk(r'Prompts/challenge1/'))
i = 1 
for j in range(file_count) : 
       
      pp = open ("Prompts/challenge1/p"+ str(i) +".txt","r") 
      i = i + 1 
      answer = input(pp.read()) 
      if answer == "a": 
        print("Fuck ya") 



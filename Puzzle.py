#! /usr/bin/env python3 # coding: UTF-8 

import os

prompts_count  = sum(len(files) for _, _, files in os.walk(r'Prompts/challenge1/'))
answers_count = sum(len(files) for _, _, files in os.walk(r'Prompts/answer1/')) 
i = 1 
l = 1 
score = 0 
for j in range(prompts_count) : 
       
      pp = open ("Prompts/challenge1/p"+ str(i) +".txt","r") 
      i = i + 1 
      answer = input(pp.read()) 
      for k in range(answers_count): 
        aa = open ("Prompts/answer1/a" + str(l) + ".txt","r") 
        if answer == aa : 
            score += 1 
        else: 
            continue 









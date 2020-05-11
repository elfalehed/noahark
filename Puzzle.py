#! /usr/bin/env python3 # coding: UTF-8 

import os

prompts_count  = sum(len(files) for _, _, files in os.walk(r'Prompts/challenge1/'))
answers_count = sum(len(files) for _, _, files in os.walk(r'Prompts/answer1/')) 

answers = ["a", "b", "c"] 
e = len(answers)
def puzz(): 
    i = 1 
    l = 1 
    score = 0 
    for j in range(prompts_count) : 
          pp = open ("Prompts/challenge1/p"+ str(i) +".txt","r") 
          i = i + 1 
          answer = input(pp.read()) 
          for k in range (e): 
                if answer == answers[l] : 
                  score += 1 
    print(score)    


def main(): 
    puzz() 

if __name__=='__main__': main() 





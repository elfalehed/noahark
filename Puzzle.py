#! /usr/bin/env python3 # coding: UTF-8 

import os

prompts_count  = sum(len(files) for _, _, files in os.walk(r'Prompts/challenge1/'))
answers_count = sum(len(files) for _, _, files in os.walk(r'Prompts/answer1/')) 

answers = ["a", "b", "c","45"] 
e = len(answers)
def puzz(): 
    i = 1 
    l = 1 
    c = 0 
    score = 0 
    for j in range(prompts_count) : 
          pp = open ("Prompts/challenge1/p"+ str(i) +".txt","r") 
          aa = open ("Prompts/answer1/a"+ str(i) +".txt", "r")     
          i = i + 1 
          answer = input(pp.read() )
          for k in range (e): 
                if answer == answers[c]: 
                    score += 1 
                    c = c + 1 
                elif answer != answers[c]: 
                    pass 
                else:
                    pass 
    print('Your score is =',score)    


def main(): 
    puzz() 

if __name__=='__main__': main() 





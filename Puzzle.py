#! /usr/bin/env python3 # coding: UTF-8 
# this is a shitty code 

import os, sys  
import numpy as np 
# Crypto 
from cryptography.fernet import Fernet 
# Sound 
#/from playsound import playsound
from pydub import AudioSegment 
from pydub.playback import play  
# key 
#key = Ferent.generate_key() 

# opening the needed files, a better method is always something i can appreciate
prompts_count1 =  sum(len(files) for _, _, files in os.walk(r'Prompts/challenge1/'))
promtps_count2 = sum(len(files) for _, _, files in os.walk(r'Prompts/challenge2/'))
abb = sum(len(files) for _, _, files in os.walk(r'Prompts/answer1/'))


answers1 = ["a", "b", "c","45"] 
e = len(answers1) 
# Puzz1 
def puzz1(): 

    i = 1 
    l = 1 
    c = 0 
    score = 0 
    for j in range(prompts_count1) : 
          pp = open ("Prompts/challenge1/p"+ str(i) +".txt","r") 
          # opening answers was here   
          i = i + 1 
          answer = input(pp.read() )
          aa = open ("Prompts/answer1/a" + str(i) +".txt", "r") 
          for k in range (e): 
                if answer == answers1[c]: 
                    score += 1 
                    c = c + 1 
                elif answer != answers1[c]: 
                     pass
                elif c > abb: 
                      break
                else: 
                    pass
    print('Your score is =',score)     

# Puzz2 
def puzz2():
    i = 0 
    l = 1 
    c = 0 
    score = 0 
    for j in range(prompts_count) : 
          pp = open ("Prompts/challenge2/p"+ str(i) +".txt","r") 
          # opening answers was here   
          i = i + 1 
          answer = input(pp.read() )
          aa = open ("Prompts/answer2/a" + str(i) +".txt", "r") 
          for k in range (e): 
                if answer == answers[c]: 
                    score += 1 
                    c = c + 1 
                elif answer != answers[c]: 
                    pass
                elif answers[c] > len(answers): 
                    break
                else: 
                    pass
    print('Your score is =',score)    
    
# Better Functions (Redo) 
# Better Errors Handler
"""
2Do: 
    - Document the code 
    - Re:test and make a full map
"""

def main(): 
    try:
        puzz1() 
        letter = "test"
        print(letter, end='') 
        print('')
        #playsound('oahark.mp3') 
        sound = AudioSegment.from_mp3('noahark.mp3') 
        play(sound) 
        print('\n') 
    except ValueError: 
        print("Error?") 
   # i need an errors handler over here 
if __name__=='__main__':main()

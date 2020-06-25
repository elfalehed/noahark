#! /usr/bin/env python3 

import sys, os
import random
import math
import numpy as np 

score = 0 
lives = 3 
i, j, k = 1, 0, 0
coupons = 1 

class questions: 
    def __init__(self): 
        pass 
    def first_question():
        files_count = sum(len(files) for _, _, files in os.walk(r'Adventures/q/'))
        for i in range(files_count):
            with open("/home/mohamed/Desktop/projects/NoahArk/Adventures/q/q"+str(i)+".txt","r") as f:
                content = f.read()
                print(content) 
                answer = input("$ ") 
                


if __name__=='__main__':
    with open("banner.txt") as f: 
        banner = f.read()
        print(banner,"BY @KMx404\n") 
    questions.first_question()  






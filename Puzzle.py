#! /usr/bin/env python3  # coding: UTF-8
# This shit is coded by @KMx404, I guess you can tell by my github repository XD
#2Do: 
# - Check how the return statement actually work. Cause the main problem starts over there.

# The basic idea is gonna be like this : 


#class qess: 

   # def __init__(self, score): 
   #     self.score = score

def ask1(score,pp)  : 
    pp = open("Prompts/challenge1/p1.txt","r") 
    answer = input(pp.read()) 
    if answer == "a" : 
       score = score + 1 
    return score #as int(into)               

def ask2(score, pp2): 
    pp2 =  open("Prompts/challenge1/p2.txt","r") 
    answer = input(pp2.read()) 
    if answer == "b" : 
        score = score + 1 
    return score  #s int(binto) 


# i need to know how to import a function that is inside another function 
def main():   
     score = 0 
     #print(score.ask1()) 
     pp = open("Prompts/challenge1/p1.txt", "r") 
     sc1 = ask1(score,pp) 
     pp2 = open("Prompts/challenge1/p2.txt", "r") 
     sc2 = ask2(score, pp2) 
     print("You've got " + str(sc1+sc2) + "/" + "2")


if __name__=='__main__':main() 





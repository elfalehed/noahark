#! /usr/bin/env python3  # coding: UTF-8
# This shit is coded by @KMx404, I guess you can tell by my github repository XD

questions_prompt = [ 
        ' Do you think you are  smart enough to excel NoahArk game ?\n a) Yes\n b) Maybe\n c) I dont know\n',
        ' What is life ?\n a) Knowledge\n b) Art\n c) Freedom '   ] 

questions_answer = [ 
        "a", 
        "a"
                   ]       
def run_test(questions_prompt, questions_answer): 
    qu = 0 
    for ques in questions_prompt: 
        qu += 1 
        answer = raw_input(questions_prompt[qu]) 
        if answer == questions_answe[qu]: 
            qu += 1 

run_test(questions_prompt, questions_answer)

#! /usr/bin/env python3   

from TheBase import Questions
from Questions import questions   

questions_prompt = [ 
"Do you think you're smart/intelligent ? \n a) Yes\n b) No\n c) I don't know\n",
"You think of the rules as? \n a) Follow \n b) Break\n c) Ignore\n", 
"What's life? \n a) Knowledge\n b) Freedom \n c) Art?\n d) Something else\n ",
        ] 

questions_asked1 = [ 
        questions(questions_prompt[0], "a"), 
        questions(questions_prompt[1], "c"),
        questions(questions_prompt[2],"d"),
        ] 

def run_test(questions_asked): 
    score = 0 
    for ques in questions_asked: 
        answer = raw_input(question.prompt) 
        if answer == question.answer: 
        score += 1 
    print("You got " + str(score) + "/" + str(len(questions_prompt))

# There's gonna be levels 
# The run test function are gonna be copied with different handle & new promptss and new questions_asked2 

run_test()


#! /usr/bin/env python3 

import sys, time, random


# Slow Display 
typing_speed = 50
def slow_type(str): 
    for letter in str:
        sys.stdout.write(letter) 
        sys.stdout.flush()
        time.sleep(0.1) 

slow_type("\ntest this gonna need to be a full testing paragraph in order to see the full potential *wrong grammar?") 






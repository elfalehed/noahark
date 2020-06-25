#! /usr/bin/env python3 #UTF-8 
#@KMx404
import os, sys
import glob
import errno
cp = sum(len(files) for _, _, files in os.walk(r'/Prompts/')) 
for i in range(cp): 
    path = '/home/mohamed/Desktop/projects/NoahArk/Prompts/challenge[i]/*.txt' #note C:
    files = glob.glob(path)
    for name in files:
        try:
           with open(name) as f:
              for line in f:
                  print(line.split())
        except IOError as exc: #Not sure what error this is
              if exc.errno != errno.EISDIR:
                   raise



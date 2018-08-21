'''
Created on Apr 20, 2018

@author: dario
'''

# Project: Simple countdown Program

# countdown.py - A simple countdown script.

import time, subprocess

# Step 1: Count Down
timeLeft = 60
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1

# Step 2: Play the Sound File
subprocess.Popen(['start', 'alarm.wav'], shell=True)  # alarm.wav: 1: alarm.wav: start: not found

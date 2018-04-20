'''
Created on Apr 19, 2018

@author: dario

Project: Super Stopwatch

Step 1: Set Up the Program to Track Times
Step 2: Track and Print Lap Times

'''

# stopwatch.py - A simple stopeatch program.

import time

# Display the program instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch.' \
      '\nPress Ctrl-C to quit.')

input()  # Press ENTER to begin.

print('Started.')

startTime = time.time()  # get the first lap's start time
lastTime = startTime
lapNum = 1

# Start tracking the lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        
        print('Lap #{}: {} ({})'.format(lapNum, totalTime, lapTime))
        
        lapNum += 1
        lastTime = time.time()  # reset the lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')
    

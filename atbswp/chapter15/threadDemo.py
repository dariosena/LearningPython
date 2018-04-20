'''
Created on Apr 19, 2018

@author: dario
'''

import threading, time

print("Start of program.")


def takeANap():
    time.sleep(5)
    print("Wake up!")

    
threadObj = threading.Thread(target=takeANap)
threadObj.start()

print("End of program.")

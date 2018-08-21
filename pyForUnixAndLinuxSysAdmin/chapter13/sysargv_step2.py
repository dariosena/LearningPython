'''
Created on Apr 20, 2018

@author: dario
'''

import sys

# python sysargv_step2.py
# python sysargv_step2.py foo
# python sysargv_step2.py foo bad for you

# Python indexes start at Zero, so let's not count the command itself wich is
# sys.argv[0]
num_arguments = len(sys.argv) - 1

# If there are no arguments to the command, send a message to standard error.
if num_arguments == 0:
    sys.stderr.write("Hey, type in an option silly.\n")
else:
    print(sys.argv, "You typed in", num_arguments, "arguments.")

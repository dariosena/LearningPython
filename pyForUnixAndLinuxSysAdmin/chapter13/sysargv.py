'''
Created on Apr 20, 2018

@author: dario
'''

import sys

# python sysargv.py
# python sysargv.py foo
# python sysargv.py foo bad for you

# Python indexes start at Zero, so let's not count the command itself wich is
# sys.argv[0]

num_arguments = len(sys.argv) - 1
print(sys.argv, "You typed in", num_arguments, "arguments.")

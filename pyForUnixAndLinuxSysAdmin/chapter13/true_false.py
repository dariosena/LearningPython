'''
Created on Apr 20, 2018

@author: dario
'''

import optparse
import os

# # True/False Usage Pattern


def main():
    p = optparse.OptionParser(description="Python 'ls' command clone",
                              prog="pyls",
                              version="0.1a",
                              usage="%prog [directory]")
    
    p.add_option("--verbose", "-v", action="store_true",
                 help="Enables Verbose Output", default=False)
    
    options, arguments = p.parse_args()
    
    if len(arguments) == 1:
        if options.verbose:
            print("Verbose Mode Enabled")
        
        path = arguments[0]
        
        for filename in os.listdir(path):
            if options.verbose:
                print("Filename: {} ".format(filename))
            else:
                print(filename)
    else:
        p.print_help()


if __name__ == "__main__":
    main()

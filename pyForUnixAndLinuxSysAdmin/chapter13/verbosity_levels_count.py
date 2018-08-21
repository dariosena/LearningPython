'''
Created on Apr 21, 2018

@author: dario
'''

import optparse
import os

# # Counting Options Usage Pattern


# using auto-incremented count design pattern
def main():
    p = optparse.OptionParser(description="Python 'ls' command clone",
                              prog="pyls",
                              version="0.1a",
                              usage="%prog [directory]")
    
    p.add_option("-v", action="count", dest="verbose")
    options, arguments = p.parse_args()
    
    if len(arguments) == 1:
        if options.verbose:
            print("Verbose Mode Enabled at Level: {}".format(options.verbose))
        
        path = arguments[0]
        for filename in os.listdir(path):
            if options.verbose == 1:
                print("Filename: {} ".format(filename))
            elif options.verbose == 2:
                fullpath = os.path.join(path, filename)
                print("Filename: {} | Byte Size: {}".format(
                    filename, os.path.getsize(fullpath)))
            else:
                print(filename)
    else:
        p.print_help()


if __name__ == "__main__":
    main()

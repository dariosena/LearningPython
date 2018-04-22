'''
Created on Apr 21, 2018

@author: dario
'''

import optparse
import os


def main():
    p = optparse.OptionParser(description="Lists contents of two directories",
                              prog="pymultils",
                              version="0.1a",
                              usage="%prog [--dir dir1 dir2]")
    
    p.add_option("--dir", action="store", dest="dir", nargs=2)
    
    options, _ = p.parse_args()
    
    if options.dir:
        for dir in options.dir:
            print("Listing of {}:\n".format(dir))
            for filename in os.listdir(dir):
                print(filename)
    else:
        p.print_help()

    
if __name__ == "__main__":
    main()

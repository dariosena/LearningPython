'''
Created on Apr 20, 2018

@author: dario
'''

import optparse

# # Introduction to Optparse


def main():
    p = optparse.OptionParser()
    p.add_option("--sysadmin", "-s", default="BOFH")
    options, arguments = p.parse_args()
    print("Hello, {}.".format(options.sysadmin))


if __name__ == '__main__':
    main()

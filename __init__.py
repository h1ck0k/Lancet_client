#!/usr/bin/python

"""
This is the initialization file for the Lancet program.
"""

#Metadata
__developer__ = "Christopher Breitenstein"
__liscense__ = "MIT"
__Version__ = '1.0.0'


#external dependancies

from main import main as lancet

#Functions

def main():

    checkForUpdate()

    getVersion()

    lancet()

def getVersion():

    pass

def checkForUpdate():

    pass


#Variables



#main

if __name__ == "__main__":
    main()

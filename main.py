#!/usr/bin/python

"""
This is the main file for the Lancet program.
"""

# Metadata
__developer__= "Christopher Breitenstein"
__liscense__= "MIT"
__Version__ = '1.0.0'
__applicationName__= "Lancet"


# external dependancies



# Variables

logon = ["%s version %s" % (__applicationName__, __Version__)]

logo = ["",
        "LancetLancetLancetLaNLancet                               | %s version %s" % (__applicationName__, __Version__),
        " ancetLanceT        LancetLancetLancet                    |",
        "  ncetLancE        TLanceTLancetLancetLancet              | developed by %s"%__developer__,
        "   cetTlaN        CetLancetLancetLancetLancetLanc         |",
        "    etEtL        AncetLancetLancetLancetLancetLancetLa    |",
        "    etAn        CetLancetLancetLancetLancetLancetLancet   |",
        "   cetC               EtLanCetLancetLancetLancetLancet    |",
        "  ncetL               AncetLancetLancetLancetLancet       |",
        " ancetC               EtLancetLancetLancetLancet          |",
        "LancetLancetLancetLancetLancetLancetLancet                |",
        ""]

# Functions

def main():
    generteOpening()

    

def generteOpening():

    [print(x) for x in logo]

# main

if __name__ == "__main__":
    main()

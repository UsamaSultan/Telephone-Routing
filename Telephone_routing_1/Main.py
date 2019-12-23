
""" Main """

import sys
import xlrd
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from comparisonfile import ala_comparsion as ac

if __name__ == '__main__':

    print("-1 for exit")
    while True:
        
        inp = str(input("\nDialing Number:"))
        
        if inp == '-1':
            
            print("Bye Bye..!")
            break
            
        else:

            ac.comparison(inp)


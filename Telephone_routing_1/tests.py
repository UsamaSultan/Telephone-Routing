
""" UNIT TESTING OF THE COMPLETE PROGRAM """

import xlrd
import os
import unittest
from comparisonfile import ala_comparsion as ac


class unittesting(unittest.TestCase):
    
    """ This is a fixture test case. Do not uncomment """
    
    # def setUp(self):
    """ Fixture that creates a file for input purposes """
        
    #     self.file_name = "D:\Task_Approach_1\input.xlsx"
        
    #     wb = xlrd.open_workbook(self.file_name)
        
    #     sheet = wb.sheet_by_index(0)
    
    
    # def tearDown(self):
    """ Fixture that deletes the files used for input purposes """
    #     try:
    #         os.remove(self.file_name)
    #     except: 
    #         pass
    
   
    
    def test_comparison_function(self):
        
        ac.comparison(1)
        
        # self.setUp()
        # self.tearDown()
     
     
    # def test_line_count(self):
    """ TESTING LINE COUNT """
                
    #     self.assertEqual(self.get_lines(self.file_name), 30)    

unittest.main()

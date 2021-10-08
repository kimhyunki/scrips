#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import gspread
import re

gc = gspread.oauth()

#sh = gc.create('A new spreadsheet for python')
sh = gc.open('A new spreadsheet for python')

# select worksheet by index. Worksheet indexes start from zero
worksheet = sh.get_worksheet(0)

# Most common case: Sheet1
#worksheet = sh.sheet1

# Get a list of all worksheets
#worksheet_list = sh.worksheets()

#list_of_lists = worksheet.get_values()

#find a cell with exact string value
#cell = worksheet.find("khk")
cell = worksheet.find("Dough")

print("Found something at R%sC%s" % (cell.row, cell.col))

#amount_re = re.compile(r'(Big) dough')

#cell = worksheet.find(amount_re)
#print("Found something at R%sC%s" % (cell.row, cell.col))




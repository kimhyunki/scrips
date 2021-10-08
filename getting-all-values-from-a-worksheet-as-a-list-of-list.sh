#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import gspread

gc = gspread.oauth()

#sh = gc.create('A new spreadsheet for python')
sh = gc.open('A new spreadsheet for python')

# select worksheet by index. Worksheet indexes start from zero
worksheet = sh.get_worksheet(2)

# Most common case: Sheet1
#worksheet = sh.sheet1

# Get a list of all worksheets
#worksheet_list = sh.worksheets()

list_of_lists = worksheet.get_values()

print("Get a list of all worksheets: %s" % (list_of_lists))



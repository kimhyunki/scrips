#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import gspread
import re

gc = gspread.oauth()

#sh = gc.create('A new spreadsheet for python')
sh = gc.open('A new spreadsheet for python')

# select worksheet by index. Worksheet indexes start from zero
worksheet = sh.get_worksheet(0)

#find all cells with string value
cell_list = worksheet.findall("Run store")

#find all cells with regexp
criteria_re = re.compile(r'(Small|Room-tiering) rug')
cell_list = worksheet.findall(criteria_re) 


print("Found cell_lst %s" %cell_list)


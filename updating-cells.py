#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import gspread
import re

gc = gspread.oauth()

#sh = gc.create('A new spreadsheet for python')
sh = gc.open('A new spreadsheet for python')

# select worksheet by index. Worksheet indexes start from zero
worksheet = sh.get_worksheet(0)

#worksheet.update('A:A', 'Bingo!')
#worksheet.update('A:B', [1,0])
worksheet.update('A1:P2', [
				[1, 2, 5, 7], 
                           	[3, 4, 6, 8]
			])



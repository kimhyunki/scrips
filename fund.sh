#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import gspread

gc = gspread.oauth()

sh = gc.open('A new spreadsheet for python')

print(sh.sheet2.get('A:A'))

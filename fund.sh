#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import gspread

gc = gspread.oauth()

sh = gc.open('MagicFormulaInfo_2021-09-24')

print(sh.sheet1.get('A1'))

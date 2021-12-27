#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import gspread
import pandas as pd
from gspread_pandas import Spread, Client

gc = gspread.oauth()

sh = gc.open('account book')
spread = Spread('account book')

worksheet = sh.worksheet(title='가계부')
dataframe = pd.DataFrame(worksheet.get_all_values())
#sortframe = dataframe.sort_values(by=2, axis=0)

#spread.df_to_sheet(dataframe, index=False, sheet='New Test Sheet', start='A1', replace=True)

#print(sh.sheet1.get(0))
#print (sh.worksheets())
#print (dataframe)
print (dataframe)

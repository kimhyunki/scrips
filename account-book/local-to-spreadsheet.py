#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import gspread
import pandas as pd
from gspread_pandas import Spread, Client

#file_name = "./binary.csv"
#df = pd.read_csv(file_name)

spread = Spread('account book')
print(spread.sheets)

df = pd.read_excel('~/Downloads/카카오뱅크_거래내역_N1861623493_2021122214172548.xlsx')

spread.df_to_sheet(df, index=False, sheet='New Test Sheet', start='A1', replace=True)

#gc = gspread.oauth()
#sh = gc.open('account book')
#worksheet = sh.add_worksheet(title="New Test Sheet", rows="200", cols="200")



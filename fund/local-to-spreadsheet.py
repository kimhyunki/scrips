#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import gspread
import pandas as pd
from gspread_pandas import Spread, Client
import xlrd
import csv

file_name = "/Users/khk/Downloads/MagicFormulaInfo_2020-12-11.xls"
#df = pd.read_excel(file_name, 'Sheet1', index_col=None)

#gc = gspread.oauth()
#
#sh = gc.create('A new spreadsheet')


def csv_from_excel(excel_file):
    workbook = xlrd.open_workbook(excel_file)
    all_worksheets = workbook.sheet_names()
    for worksheet_name in all_worksheets:
        worksheet = workbook.sheet_by_name(worksheet_name)
        with open(u'{}.csv'.format(worksheet_name), 'w', encoding="utf-8") as your_csv_file:
            wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)
            for rownum in range(worksheet.nrows):
                wr.writerow(worksheet.row_values(rownum))

csv_from_excel(file_name)



#spread.df_to_sheet(df, index=False, sheet='New Test Sheet', start='A1', replace=True)

#gc = gspread.oauth()
#sh = gc.open('account book')
#worksheet = sh.add_worksheet(title="New Test Sheet", rows="200", cols="200")



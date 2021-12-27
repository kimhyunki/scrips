#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
from __future__ import print_function
import pandas as pd
from gspread_pandas import Spread, Client

file_name = "./binary.csv"
df = pd.read_csv(file_name)

# 'Example Spreadsheet' needs to already exist and your user must have access to it
spread = Spread('test')
# This will ask to authenticate if you haven't done so before

# Display available worksheets
spread.sheets

# Save DataFrame to worksheet 'New Test Sheet', create it first if it doesn't exist
spread.df_to_sheet(df, index=False, sheet='New Test Sheet', start='A2', replace=True)
spread.update_cells('A1', 'B1', ['Created by:', 'khkraining@falinux.com'])
print(spread)
# <gspread_pandas.client.Spread - User: '<example_user>@gmail.com', Spread: 'Example Spreadsheet', Sheet: 'New Test Sheet'>

# You can now first instanciate a Client separately and query folders and
# instanciate other Spread objects by passing in the Client

client = Client()
# Assumming you have a dir called 'example dir' with sheets in it
available_sheets = client.find_spreadsheet_files_in_folders('펀드')
spreads = []
for sheet in available_sheets.get('펀드', []):
    spreads.append(Spread(sheet['id'], client=client))

print (spreads)

#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import gspread
import pandas as pd
from gspread_pandas import Spread, Client
import xlrd
import csv
from bs4 import BeautifulSoup

path = '/Users/khk/Downloads/MagicFormulaInfo_2021-12-24.xls'

# empty list
data = []

# for getting the header from
# the HTML file
list_header = []
soup = BeautifulSoup(open(path, 'rt', encoding='utf-8'), 'html.parser')
header = soup.find_all("table")[0].find("tr")

for items in header:
    try:
        list_header.append(items.get_text())
    except:
        continue

# for getting the data
HTML_data = soup.find_all("table")[0].find_all("tr")[1:]

for element in HTML_data:
    sub_data = []
    for sub_element in element:
        try:
            sub_data.append(sub_element.get_text())
        except:
            continue
    data.append(sub_data)

# Storing the data into Pandas
# DataFrame
dataFrame = pd.DataFrame(data = data, columns = list_header)

# Converting Pandas DataFrame
# into CSV file
#dataFrame.to_csv('Geeks.csv')

#file_name = "./Geeks.csv"
#df = pd.read_csv(file_name)

spread = Spread('test')
# This will ask to authenticate if you haven't done so before

# Display available worksheets
#spread.sheets

sheetname = path.split('/')

# Save DataFrame to worksheet 'New Test Sheet', create it first if it doesn't exist
spread.df_to_sheet(dataFrame, index=False, sheet=sheetname[-1], start='A1', replace=True)

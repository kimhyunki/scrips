#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import pandas as pd
from gspread_pandas import Spread, Client

from pprint import pprint as pp

# You can now first instanciate a Client separately and query folders and
# instanciate other Spread objects by passing in the Client


client = Client()
files_in_folders = client.find_spreadsheet_files_in_folders('test')

print(files_in_folders)


for key, val in files_in_folders.items():
    print ("key = {key}, value={value}". format(key=key, value=val))


#print("values={value}".    format(value=values))
#print("values[1]={value}". format(value=values[1]))



#pp (files_in_folders.get("펀드"))

#for key, val in files_in_folders.items():
#    pp ("key = {key}, value={value}". format(key=key, value=val))



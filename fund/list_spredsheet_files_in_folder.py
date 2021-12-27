#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
from __future__ import print_function
import pandas as pd
from gspread_pandas import Spread, Client, conf
import pprint

client = Client()
find_folder = client.find_folders(folder_name_query="펀드")

pprint.pprint(find_folder)

folder_id = list (find_folder[0].values())
pprint.pprint (folder_id)

list_files = client.list_spreadsheet_files_in_folder(folder_id[0])
pprint.pprint(list_files[0])



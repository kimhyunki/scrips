#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import pandas as pd
from gspread_pandas import Spread, Client

# You can now first instanciate a Client separately and query folders and
# instanciate other Spread objects by passing in the Client
client = Client()
files_in_folders = client.find_spreadsheet_files_in_folders('펀드')

print (files_in_folders)

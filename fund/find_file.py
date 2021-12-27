#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import pandas as pd
from gspread_pandas import Spread, Client

import pprint


client = Client()
list_file = client.list_spreadsheet_files("MagicFormulaInfo_2021-12-24.xls")

file_id = list (list_file[0].values())
pprint.pprint(file_id[0])

client.move_file(file_id[0], '/펀드')

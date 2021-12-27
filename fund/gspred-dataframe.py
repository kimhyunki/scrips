#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import pandas as pd
import gspread
from gspread_pandas import Spread, Client
from gspread_dataframe import get_as_dataframe, set_with_dataframe

gc = gspread.oauth()

sh = gc.open('account book')

worksheet = sh.worksheet(title='가계부')

set_with_dataframe(worksheet, df)

df2 = get_as_dataframe(worksheet)

print (df2)

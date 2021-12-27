#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

from __future__ import print_function
import gspread
import pandas as pd
from gspread_pandas import Spread, Client
import xlrd
import csv
from bs4 import BeautifulSoup
import gspread
import pprint

path = '/Users/khk/Downloads/MagicFormulaInfo_2021-12-24.xls'

sheetsplit = path.split('.')

pprint.pprint(sheetsplit[0])
sheetname = sheetsplit[0].split('/')

pprint.pprint(sheetname[-1])


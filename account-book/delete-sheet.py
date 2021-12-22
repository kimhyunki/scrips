#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import gspread

gc = gspread.oauth()

sh = gc.open('account book')

worksheet = sh.worksheet(title='A worksheet')
sh.del_worksheet(worksheet)



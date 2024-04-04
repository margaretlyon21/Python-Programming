#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 19:40:04 2024

@author: maggielyon
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import DataFrame, Series
sh_raw = pd.read_csv('movies.csv', 
   header = None, 
   names = ['Year','Title','Comic','IMDB','RT','','OpeningWeekendBoxOffice','AvgTicketPriceThatYear','EstdOpeningAttendance','USPopThatYear'])

sh = sh_raw[np.isfinite(
          sh_raw.OpeningWeekendBoxOffice)]
print(sh.head(5))

#  Output
#  Year            Title  ... EstdOpeningAttendance  USPopThatYear
# 1  1978.0         Superman  ...           3190317.521    222584545.0
# 2  1980.0      Superman II  ...           5241830.112    227224681.0
# 4  1983.0     Superman III  ...           4238843.492    233791994.0
# 5  1984.0        Supergirl  ...           1707812.202    235824902.0
# 6  1986.0  Howard the Duck  ...           1366613.477    240132887.0

# [5 rows x 10 columns]

# Normalize and scatterplot the scores
imdb_normalized = sh.IMDB / 10         
sh.insert(10,'IMDBNormalized',imdb_normalized)
rt_normalized = sh.RT/100        
sh.insert(11, 'RTNormalized', rt_normalized)
sh.plot.scatter(x ='RTNormalized', y ='IMDBNormalized')
plt.show()
print(sh[['RTNormalized','IMDBNormalized']].corr())
print(sh[['RTNormalized','IMDBNormalized']].describe())

# rq 1
print(sh[sh['Comic'] == 'DC'])

#rq 2
print(sh.loc[sh['Comic'] == 'DC', ['Year', 'Title']])

#rq 3
print(sh.loc[sh['Comic'] == 'Marvel', ['Year', 'Title']])

#rq 4
sh.plot.scatter(x = 'Year', y = 'AvgTicketPriceThatYear')

#rq5
print(sh[['Year','AvgTicketPriceThatYear']].corr())

#rq 5
print(sh['OpeningWeekendBoxOffice'].describe())








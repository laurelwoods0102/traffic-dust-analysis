import csv
from pandas import read_csv, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy import stats
import datetime
from pprint import pprint


df = read_csv('./data/data.csv', index_col='datetime')

#head = df.head(90)

init_date = datetime.datetime(2018, 1, 1)
last_date = datetime.datetime(2018, 3, 31)
date_interval = datetime.timedelta(days=1)
num_date = (last_date - init_date).days

date_list = [(init_date + date_interval * d).date() for d in range(num_date + 1)]

months = mdates.MonthLocator()
days = mdates.DayLocator()
fmt = mdates.DateFormatter('%m')



fig_t, ax_t = plt.subplots()
ax_t.plot(date_list, df['traffic'])
ax_t.set(xlabel='time (date)', ylabel='Amount of Traffic (1 Car)', title='Traffic in Seoul (2018-01 ~ 2018-03)')
ax_t.grid(True)
plt.xlim(datetime.date(2018, 1, 1), datetime.date(2018, 3, 31))

ax_t.xaxis.set_major_locator(months)
ax_t.xaxis.set_major_formatter(fmt)
ax_t.xaxis.set_minor_locator(days)
plt.gcf().autofmt_xdate()


col_index = ['SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']
color = []
plots = list()
for col in col_index:
    corr, pvalue = stats.pearsonr(df[col], df['traffic'])

    fig, ax = plt.subplots()
    if col == 'PM10' or col == 'PM25': ylabel = 'Amount of Dust (㎍/㎥)'
    else: ylabel = 'Amount of Compound (ppm)'
    
    ax.plot(date_list, df[col], color='C{}'.format(col_index.index(col)))
    ax.set(xlabel='time (date)\n Correlation with Traffic : {}'.format(corr), ylabel=ylabel, title='{0} in Seoul (2018-01 ~ 2018-03)'.format(col))    
    ax.grid(True)
    plt.xlim(datetime.date(2018, 1, 1), datetime.date(2018, 3, 31))

    ax.xaxis.set_major_locator(months)
    ax.xaxis.set_major_formatter(fmt)
    ax.xaxis.set_minor_locator(days)
    plt.gcf().autofmt_xdate()


plt.show()
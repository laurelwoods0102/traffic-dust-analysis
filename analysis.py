import csv
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from scipy import stats
import datetime
from pprint import pprint


df = read_csv('./data/data.csv', index_col='datetime')

#head = df.head(90)
#pprint(head.index)

pearson = stats.pearsonr(df['PM10'], df['PM25'])
pprint(pearson)

init_date = datetime.datetime(2018, 1, 1)
last_date = datetime.datetime(2018, 3, 31)
date_interval = datetime.timedelta(days=1)
num_date = (last_date - init_date).days

date_list = [(init_date + date_interval * d).date() for d in range(num_date + 1)]

fig, ax = plt.subplots()
ax.plot(date_list, df['traffic'])
ax.set(xlabel='time (date)', ylabel='Amount of Traffic (1 Car)', title='Traffic in Seoul')
ax.grid(True)
plt.xlim(datetime.date(2018, 1, 1), datetime.date(2018, 3, 31))

months = mdates.MonthLocator()
days = mdates.DayLocator()
fmt = mdates.DateFormatter('%m')

ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(fmt)
ax.xaxis.set_minor_locator(days)
plt.gcf().autofmt_xdate()

plt.show()


'''
# Traffic
fig_t, ax_t = plt.subplots()
ax_t.plot(df['traffic'])

ax_t.set(xlabel='time (date)', ylabel='Amount of Traffic (1 Car)', title='Traffic in Seoul')
ax_t.grid(True)

plt.show()

# SO2
fig_SO2, ax_SO2 = plt.subplots()
ax_SO2.plot(df['SO2'])

ax_SO2.set(xlabel='time (date)', ylabel='Amount of Dust (ppm)', title='Compound in Air (SO2)')
ax_SO2.grid()

# CO
fig_CO, ax_CO = plt.subplots()
ax_CO.plot(df['CO'])

ax_SO2.set(xlabel='time (date)', ylabel='Amount of Dust (ppm)', title='Compound in Air (CO)')
ax_SO2.grid()

# O3
fig_O3, ax_O3 = plt.subplots()
ax_O3.plot(df['O3'])

ax_O3.set(xlabel='time (date)', ylabel='Amount of Dust (ppm)', title='Compound in Air (O3)')
ax_O3.grid()

# NO2
fig_NO2, ax_NO2 = plt.subplots()
ax_NO2.plot(df['NO2'])

ax_NO2.set(xlabel='time (date)', ylabel='Amount of Dust (ppm)', title='Compound in Air (NO2)')
ax_NO2.grid()

# PM10 & PM25
fig_PM, ax_PM = plt.subplots()
ax_PM.plot(df['PM10'], 'b-', df['PM25'], 'r-')

ax_PM.set(xlabel='time (date)', ylabel='Amount of Dust (ppm)', title='Compound in Air (PM10, PM25)')
ax_PM.grid()



plt.show()
'''
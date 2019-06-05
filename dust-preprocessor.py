import os
import numpy
import pandas
import csv
import datetime
from pprint import pprint

init_date = datetime.datetime(2018, 1, 1)
last_date = datetime.datetime(2018, 3, 31)
date_interval = datetime.timedelta(days=1)
hour_interval = datetime.timedelta(hours=1)
num_date = (last_date - init_date).days

raw_date_list = [str((init_date + date_interval * d).date()).replace('-', '') for d in range(num_date + 1)]
hours_list = [str(format(h+1, '02')) for h in range(24)]

index_datetime = list()
for rdl in raw_date_list:
    for hl in hours_list:
        index_datetime.append(rdl + hl)

column_index = ['SO2', 'CO', 'O3', 'NO2', 'PM10', 'PM25']

dataset = list()
for id_dt in index_datetime:
    df = pandas.read_csv('./data/dust/{}.csv'.format(id_dt), names=column_index)
    df_mean = df.mean(axis=0, skipna=True)
    dataset.append(df_mean)

processed_data = pandas.concat(dataset, axis=1)
processed_data = processed_data.rename(index=str, columns={index_datetime.index(x): x for x in index_datetime})
processed_data.to_csv('./data/dust.csv', mode='w')
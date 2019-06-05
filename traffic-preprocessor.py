import os
import numpy
import pandas
import csv
import datetime
from pprint import pprint

init_date = datetime.datetime(2018, 3, 1)
last_date = datetime.datetime(2018, 3, 31)
date_interval = datetime.timedelta(days=1)
hour_interval = datetime.timedelta(hours=1)
num_date = (last_date - init_date).days

raw_date_list = [str((init_date + date_interval * d).date()).replace('-', '') for d in range(num_date + 1)]


dataset = list()
for rdl in raw_date_list:
    df = pandas.read_csv('./data/traffic/{0}.csv'.format(rdl))
    df_sum = df.sum(axis=1, skipna=True)
    df_mean = df_sum.mean(axis=0, skipna=True)
    dataset.append(df_mean)

processed_data = pandas.DataFrame(dataset, index=raw_date_list)
pprint(processed_data)
processed_data.to_csv('./data/traffic_3.csv', mode='w')
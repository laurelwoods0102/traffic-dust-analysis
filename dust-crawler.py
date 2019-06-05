import csv
import json
from collections import defaultdict
import datetime
from pprint import pprint

doc = open("./raw_data/dust/2018년 1분기-서울시.csv", 'r', encoding='utf-8-sig', newline='')
reader = csv.reader(doc)
rows = (row for row in reader)

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


data = defaultdict(lambda: list())
for row in rows:
    if row[0] == "지역": continue
    data[str(row[3])].append(row[4:10])

for id_dt in index_datetime:
    with open("./data/dust/{}.csv".format(id_dt), 'w', encoding='utf-8', newline='') as result:
        wr = csv.writer(result)
        for info in data[id_dt]: wr.writerow(info)           
doc.close()
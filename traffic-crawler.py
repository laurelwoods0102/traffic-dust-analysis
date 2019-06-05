import csv
import json
from collections import defaultdict
import datetime
from pprint import pprint

doc = open('./raw_data/traffic/2018년 3월 서울시 교통량 조사자료.csv', 'r', encoding='utf-8-sig', newline='')
reader = csv.reader(doc)
rows = (row for row in reader)

init_date = datetime.datetime(2018, 3, 1)
last_date = datetime.datetime(2018, 3, 31)
date_interval = datetime.timedelta(days=1)
hour_interval = datetime.timedelta(hours=1)
num_date = (last_date - init_date).days

raw_date_list = [str((init_date + date_interval * d).date()).replace('-', '') for d in range(num_date + 1)]

data = defaultdict(lambda: list())
for row in rows:
    if row[0] == "일자": continue
    data[str(row[0])].append(row[6:31])

for rdl in raw_date_list:
    with open("./data/traffic/{}.csv".format(rdl), 'w', encoding='utf-8', newline='') as result:
        wr = csv.writer(result)
        for info in data[rdl]: wr.writerow(info)           
doc.close()
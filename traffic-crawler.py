import csv
import json
from collections import defaultdict
import datetime
from pprint import pprint

doc = open('./raw_data/traffic/2018년 1월 서울시 교통량 조사자료.csv', 'r', encoding='utf-8-sig', newline='')
reader = csv.reader(doc)
rows = (row for row in reader)

init_date = datetime.datetime(2018, 1, 1)
last_date = datetime.datetime(2018, 1, 31)
date_interval = datetime.timedelta(days=1)
hour_interval = datetime.timedelta(hours=1)
num_date = (last_date - init_date).days


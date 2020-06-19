import json
import csv
from datetime import datetime
import os
import pathlib

def dt_num2csv(class_name):
    filename = datetime.now().strftime("%Y%m%d")
    awareness_time = datetime.now().strftime("%Y%m%d%H%M%S")
    if os.path.exists(filename + '.csv'):
        with open(filename + '.csv', mode='a') as f:
            f.write(awareness_time + ',' + class_name + '\n')
    else:
        with open(filename + '.csv', mode='w') as f:
            f.write(awareness_time + ',' + class_name + '\n')

def csv2json():
    json_list = []
    keys = ('date', 'label')

    with open('20200601.csv', 'r') as f:
        for row in csv.DictReader(f, keys):
            json_list.append(row)

    with open('output.json', 'w') as f:
        json.dump(json_list, f)

    with open('output.json', 'r') as f:
        json_output = json.load(f)
from __future__ import absolute_import, division, print_function, unicode_literals
import json
import pandas as pd

f = open('data.txt')
data = json.load(f)

for x in data:
    print(x)

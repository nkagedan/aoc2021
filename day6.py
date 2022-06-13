#<codecell>
'''Load Input Data'''

import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()

file = os.environ['filename']

with open(file, 'r') as file:
    data = file.read().strip()

#input_list = data.splitlines()
input_list = [int(i) for i in data.split(',')]
#df = pd.DataFrame(input_list, columns =['raw_input'])

#<codecell>

'''Parts 1 and 2'''

days = 256

df=pd.DataFrame(np.zeros([9,2]).astype('int64'), columns=['fish_count','temp'])

for i in input_list:
    df.iloc[i]['fish_count'] += 1

for day in range(days):
    for i in df.index:
        if i > 0:
            df.iloc[i-1]['temp'] = df.iloc[i]['fish_count']
    df.iloc[6]['temp'] += df.iloc[0]['fish_count']
    df.iloc[8]['temp'] = df.iloc[0]['fish_count']
    df['fish_count'] = df['temp']

result = np.int64(0)

result = df['fish_count'].sum()

print(f'{result=}')
#<codecell>

'''Part 2'''

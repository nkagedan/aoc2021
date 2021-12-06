'''Load Input Data'''

import pandas as pd

file = 'input5test.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
df = pd.DataFrame(input_list, columns =['raw_input'])

'''Part 1'''

df['split'] = df['raw_input'].str.split(pat=',')
df['x1']=df['raw_input'].str.split(pat=',').str[0].astype(int)
df['y1']=df['raw_input'].str.split(pat=',').str[1].str.split(pat=' -> ').str[0].astype(int)
df['x2']=df['raw_input'].str.split(pat=',').str[1].str.split(pat=' -> ').str[1].astype(int)
df['y2']=df['raw_input'].str.split(pat=',').str[2].astype(int)


df = df.loc[(df['x1'] == df['x2']) | (df['y1'] == df['y2'])]
df


'''Part 2'''

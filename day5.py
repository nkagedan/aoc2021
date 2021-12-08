'''Load Input Data'''

import pandas as pd
import numpy as np

file = 'input5test.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
df = pd.DataFrame(input_list, columns =['raw_input'])

'''Part 1'''

df['x1']=df['raw_input'].str.split(pat=',').str[0].astype(int)
df['y1']=df['raw_input'].str.split(pat=',').str[1].str.split(pat=' -> ').str[0].astype(int)
df['x2']=df['raw_input'].str.split(pat=',').str[1].str.split(pat=' -> ').str[1].astype(int)
df['y2']=df['raw_input'].str.split(pat=',').str[2].astype(int)


df = df.loc[(df['x1'] == df['x2']) | (df['y1'] == df['y2'])]
df

df[['x1','x2']].values.max()

grid = pd.DataFrame(np.zeros((df[['x1','x2']].values.max()+1,df[['y1','y2']].values.max()+1)), dtype=int)

grid

def plot_line(row):
    if row['x1'] == row['x2']:
        
    elif row['y1'] == row['y2']:
    else:
        pass

for i in range(len(df)):
    print(f'{i=}')
    print(type(df.iloc[i]))


'''Part 2'''

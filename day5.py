'''Load Input Data'''

import pandas as pd
import numpy as np

file = 'input5.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
df = pd.DataFrame(input_list, columns =['raw_input'])

'''Part 1'''

def plot_line(row):
    if row['x1'] == row['x2']:
        grid.iloc[min(row[['y1', 'y2']]):max(row[['y1','y2']]+1),row['x1']] +=1
    elif row['y1'] == row['y2']:
        grid.iloc[row['y1'],min(row[['x1','x2']]):max(row[['x1','x2']])+1] +=1
    else:
        range(min(row.x1, row.x2),max(row.x1, row.x2))



df['x1']=df['raw_input'].str.split(pat=',').str[0].astype(int)
df['y1']=df['raw_input'].str.split(pat=',').str[1].str.split(pat=' -> ').str[0].astype(int)
df['x2']=df['raw_input'].str.split(pat=',').str[1].str.split(pat=' -> ').str[1].astype(int)
df['y2']=df['raw_input'].str.split(pat=',').str[2].astype(int)

df['y2'].values.max()
df.shape

grid = pd.DataFrame(np.zeros((df[['x1','x2']].values.max()+5,df[['y1','y2']].values.max()+5)), dtype=int)


for i in range(len(df)):
    pass
    plot_line(df.iloc[i])

grid
result = 0

for index, row in grid.iterrows():
    for i in row.to_list():
        if i >= 2:
            result += 1

print(result)


'''Part 2'''

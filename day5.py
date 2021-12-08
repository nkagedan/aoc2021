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
        pass


df['x1']=df['raw_input'].str.split(pat=',').str[0].astype(int)
df['y1']=df['raw_input'].str.split(pat=',').str[1].str.split(pat=' -> ').str[0].astype(int)
df['x2']=df['raw_input'].str.split(pat=',').str[1].str.split(pat=' -> ').str[1].astype(int)
df['y2']=df['raw_input'].str.split(pat=',').str[2].astype(int)

grid = pd.DataFrame(np.zeros((df[['x1','x2']].values.max()+5,df[['y1','y2']].values.max()+5)), dtype=int)


for i in range(len(df)):
    plot_line(df.iloc[i])

grid
result = 0

for index, row in grid.iterrows():
    for i in row.to_list():
        if i >= 2:
            result += 1

print(f'Part 1 result = {result}')


'''Part 2'''

def plot_line2(row):
    if row['x1'] == row['x2']:
        grid.iloc[min(row[['y1', 'y2']]):max(row[['y1','y2']]+1),row['x1']] +=1
    elif row['y1'] == row['y2']:
        grid.iloc[row['y1'],min(row[['x1','x2']]):max(row[['x1','x2']])+1] +=1
    else:
        if row.y1 < row.y2:
            ys = list(range(row.y1, row.y2+1,1))
        else:
            ys = list(range(row.y1, row.y2-1,-1))
        if row.x1 < row.x2:
            xs = list(range(row.x1, row.x2+1,1))
        else:
            xs = list(range(row.x1, row.x2-1,-1))
        coordinates = list(zip(ys, xs))
        for i in coordinates:
            grid.iat[i[0], i[1]] += 1

grid = pd.DataFrame(np.zeros((df[['x1','x2']].values.max()+5,df[['y1','y2']].values.max()+5)), dtype=int)

result = 0

for i in range(len(df)):
    plot_line2(df.iloc[i])

for index, row in grid.iterrows():
    for i in row.to_list():
        if i >= 2:
            result += 1

print(f'Part 2 result = {result}')
print(grid)

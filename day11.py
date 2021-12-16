#<codecell>
'''Setup'''

import pandas as pd
import numpy as np
import pprint
pp = pprint.PrettyPrinter(indent=4)
import json

file = 'input11test.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
#input_list = [int(i) for i in data.split(',')]
#df = pd.DataFrame(input_list, columns =['raw_input'])
df = pd.DataFrame(np.zeros([len(input_list),len(input_list[0])], dtype=int))
for i in range(len(input_list)):
    df.loc[i] = [int(x) for x in list(input_list[i])]

#<codecell>

'''Part 1'''

df

df += 1

df.values.max()

while df.values.max() >= 10:



for y in list(df.index):
    for x in list(dt.columns):
        coordinates = [y, x]
        if df.iloc[y][x] == 10:
            flash(coordinates)


def flash(coordinates):
    y = coordinates[0]
    x = coordinates[1]
    to_increment = []
    for i in range(y-1,y+2):
        for j in range(x-1,x+2):
            to_increment.append([i,j])
    print(f'{to_increment=}')
    for cell in to_increment:
        df.iloc[cell[0],cell[1]] += 1
        print(df.iloc[cell[0],cell[1]])

flash([0,0])            

df



#<codecell>

'''Part 2'''

#<codecell>

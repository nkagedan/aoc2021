#<codecell>
'''Setup'''

import pandas as pd
import numpy as np
import pprint
pp = pprint.PrettyPrinter(indent=4)
file = 'input9.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
#input_list = [int(i) for i in data.split(',')]
df = pd.DataFrame(input_list, columns =['raw_input'])


#<codecell>

'''Part 1'''
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 10)


df = pd.DataFrame(np.zeros([len(input_list),len(input_list[0])], dtype=int))


for i in range(len(input_list)):
    df.loc[i] = [int(x) for x in list(input_list[i])]

risk_level = 0
cells_checked = 0

for y in range(len(df)):
    for x in df.columns:
        cells_checked += 1
        #print(f'{y=} {x=}')
        target = int(df.iat[y,x])
        search_area = df.iloc[max(0,(y-1)):(y+2),max(0,(x-1)):(x+2)].stack().tolist()
        if target == min(search_area) and target != 9:
            print(f'adding {target+1} at {y=} {x=}')
            risk_level += (target+1)

print(f'{risk_level=}')
print(f'{df.shape=}, {cells_checked=}')

#<codecell>

'''Part 2'''

df

visited = []
basin_size = 0

def find_basin_size(coordinates,visited,df):
    if coordinates not in visited and df.iat[coordinates] != 9:
        basin_size += 1
        visited.append(coordinates)
        search_area = df.iloc[max(0,(y-1)):(y+2),max(0,(x-1)):(x+2)]
        for neighbor in search_area:
            find_basin_size(neighbor)




#<codecell>

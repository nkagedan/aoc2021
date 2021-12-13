#<codecell>
'''Setup'''

import pandas as pd
import numpy as np
import pprint
pp = pprint.PrettyPrinter(indent=4)
file = 'input9test.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
#input_list = [int(i) for i in data.split(',')]
df = pd.DataFrame(input_list, columns =['raw_input'])


#<codecell>

'''Part 1'''
pd.set_option('display.max_rows', 20)
pd.set_option('display.max_columns', 20)


df = pd.DataFrame(np.zeros([len(input_list),len(input_list[0])], dtype=int))


for i in range(len(input_list)):
    df.loc[i] = [int(x) for x in list(input_list[i])]

risk_level = 0
cells_checked = 0
targets = []

for y in range(len(df)):
    for x in df.columns:
        cells_checked += 1
        target = int(df.iat[y,x])
        search_area = df.iloc[max(0,(y-1)):(y+2),max(0,(x-1)):(x+2)].stack().tolist()
        if target == min(search_area) and target != 9:
            risk_level += (target+1)
            coordinates = [y,x]
            targets.append(coordinates)

print(f'{risk_level=}')
print(f'{df.shape=}, {cells_checked=}')

#<codecell>

'''Part 2'''

#<codecell>

def find_basin_size(coordinates, visited, df, basin_size):

    y = coordinates[0]
    x = coordinates[1]

    if coordinates not in visited and df.iat[y,x] != 9:
        visited.append(coordinates)
        basin_size[0] += 1
        neighbors = [[max(0,y-1),x],[min(df.shape[0]-1,y+1),x],[y,max(0,x-1)],[y,min(df.shape[1]-1,x+1)]]
        for neighbor in neighbors:
            find_basin_size(neighbor, visited, df, basin_size)
    else:
        return 0

    return visited

basin_size_list = []

for target in targets:
    visited = []
    basin_size = [0]
    basin_size_list.append(len(find_basin_size(target,visited,df,basin_size)))

x=sorted(basin_size_list, reverse = True)
result = np.prod(x[:3])
result




#<codecell>

def find_basin_size_inc(coordinates, visited, df, basin_size):
    print(f'about to start checking: {coordinates}; current basin size is {basin_size}\n')
    y = coordinates[0]
    x = coordinates[1]
    #print(f'value at this location is {df.iat[y,x]}')
    print(f'locations we have visited before now are: {visited=}\n')
    if coordinates not in visited and df.iat[y,x] != 9:
        print('triggered "if" statement, will now increment basin_size\n')
        basin_size += 1
        print(f'{basin_size=} after increment; adding these coordinates to "visited"\n')
        visited.append(coordinates)
        neighbors = [[max(0,y-1),x],[min(df.shape[0]-1,y+1),x],[y,max(0,x-1)],[y,min(df.shape[1]-1,x+1)]]
        print(f'neighbors to check: {neighbors=}\n')
        for neighbor in neighbors:
            basin_size += int(find_basin_size_inc(neighbor, visited, df, basin_size))
        print(f'done with for loop from {coordinates=} and proceeding to return basin_size\n')
    else:
        print(f'did not trigger if statement, so will return 0\n')
        return 0

    print(f'about to return {basin_size=}\n')
    return basin_size

visited = []
basin_size = 0
x=0

x = find_basin_size_inc([0,0], visited, df, basin_size)
print(x)

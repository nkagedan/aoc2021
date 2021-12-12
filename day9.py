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

df.shape
df

def find_basin_size(coordinates, visited, df, basin_size):
    pass
    print(f'{basin_size=}')
    print(coordinates)
    y = coordinates[0]
    x = coordinates[1]
    print(f'{df.iat[y,x]=}')
    print(f'{visited=}')
    if coordinates not in visited and df.iat[y,x] != 9:
        pass
        print('triggered "if" statement')
        basin_size += 1
        print(f'after increment, {basin_size=}')
        visited.append(coordinates)
        neighbors = [[max(0,y-1),x],[min(df.shape[0]-1,y+1),x],[y,max(0,x-1)],[y,min(df.shape[1]-1,x+1)]]
        for neighbor in neighbors:
            pass
            basin_size += int(find_basin_size(neighbor, visited, df, basin_size))

        print(f'about to return {basin_size=}')
        return basin_size

#<codecell>
visited = []
basin_size = 0
x=0

x = find_basin_size([3,1], visited, df, basin_size)
print(x)




#<codecell>

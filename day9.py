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

input_list
df
len(input_list[0])

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
        if target == min(search_area):
            print(f'adding {target+1} at {y=} {x=}')
            risk_level += (target+1)

print(risk_level)
print(f'{df.shape=}, {cells_checked=}')

df.iloc[max(0,(0-1)):(0+2),max(0,(0-1)):(0+2)]

df.iloc[0:2,0:2]

df
#<codecell>

'''Part 2'''



#<codecell>

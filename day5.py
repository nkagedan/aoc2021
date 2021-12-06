'''Load Input Data'''

import pandas as pd

file = 'input5test.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
df = pd.DataFrame(input_list, columns =['raw_input'])

df

df['split'] = df['raw_input'].str.split(pat=',')
df['x1']=df['split1'].astype(str).str[0]
df['x1']=df['split1'].str[0]
df['y1']=df['split1'][1].split(' -> ')[0]
df['x2']=df['split1'][1].split(' -> ')[1]

df['raw_input'][1].split()
'''Part 1'''



'''Part 2'''

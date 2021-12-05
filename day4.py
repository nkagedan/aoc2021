'''Load Input Data'''

import pandas as pd

file = 'input4.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
input_list
df = pd.DataFrame(input_list, columns =['raw_input'])


'''Part 1'''

df.head(20)

bingo_list = df['raw_input'][0].split(',')

df.shape

# Generate bingo boards

pd.DataFrame(df['raw_input'][2].split())

l1 = df.iloc[2]['raw_input'].strip().split()
l2 = df.iloc[3]['raw_input'].split()
l3 = df.iloc[4]['raw_input'].split()
l4 = df.iloc[5]['raw_input'].split()
l5 = df.iloc[6]['raw_input'].split()

new_df = pd.DataFrame([l1,l2,l3,l4,l5])
new_df.iloc[0,1]
new_df

df.head(20)


'''Part 2'''

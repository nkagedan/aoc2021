#<codecell>
'''Load Input Data'''

import pandas as pd
import numpy as np

file = 'input8.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
#input_list = [int(i) for i in data.split(',')]
#df = pd.DataFrame(input_list, columns =['raw_input'])
input_list
#<codecell>

'''Part 1'''

unique_char_counts = [2, 4, 3, 7]

count = 0

for i in input_list:
    output_chars = i.split('|')[1].strip().split()
    for x in output_chars:
        if len(x) in unique_char_counts:
            count += 1

print(count)


#<codecell>

'''Part 2'''







#<codecell>

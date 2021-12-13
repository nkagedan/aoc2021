#<codecell>
'''Setup'''

import pandas as pd
import numpy as np
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = 'input10test.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
#input_list = [int(i) for i in data.split(',')]
#df = pd.DataFrame(input_list, columns =['raw_input'])

#<codecell>

'''Part 1'''

input_list

character_sets = {'(':')','[':']','{':'}','<':'>'}
pp.pprint(character_sets)

for i in input_list:
    print(sorted(i))
    for char in sorted(i):
        pass#print(char)
    print('\n\n\n')

#<codecell>

'''Part 2'''


#<codecell>

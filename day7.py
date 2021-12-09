#<codecell>
'''Load Input Data'''

import pandas as pd
import numpy as np

file = 'input7.txt'

with open(file, 'r') as file:
    data = file.read().strip()

#input_list = data.splitlines()
input_list = [int(i) for i in data.split(',')]
#df = pd.DataFrame(input_list, columns =['raw_input'])

#<codecell>

'''Part 1'''
def gauss(number):
    result = (number/2)*(number+1)
    return result

input_list

chosen_position = 0
chosen_energy_required = 0

for position in range(max(input_list)):

    energy_required = 0
    for crab in input_list:
        energy_required += gauss(abs(crab-position))

    if chosen_energy_required == 0 or energy_required < chosen_energy_required:
        chosen_position = position
        chosen_energy_required = energy_required

print(f'{chosen_position=} {chosen_energy_required=}')



#<codecell>

'''Part 2'''







#<codecell>

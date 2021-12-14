#<codecell>
'''Setup'''

import pandas as pd
import numpy as np
import pprint
pp = pprint.PrettyPrinter(indent=4)
import json

file = 'input10.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
#input_list = [int(i) for i in data.split(',')]
#df = pd.DataFrame(input_list, columns =['raw_input'])

#<codecell>

'''Part 1'''

char_sets = {
    ')':'(',
    ']':'[',
    '}':'{',
    '>':'<'
}


char_vals = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

print(json.dumps(char_sets, indent=4))

def find_errors(line):
    opened_stack = []
    for char in line:
        if char in char_sets.values():
            opened_stack.append(char)
        else:
            if opened_stack[-1] != char_sets[char]:
                error_chars.append(char)
                return None
            else:
                opened_stack.pop()

error_chars = []

for i in input_list:
    find_errors(i)

result = sum([char_vals[i] for i in error_chars])

print(result)

#<codecell>

'''Part 2'''


#<codecell>

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

reverse_char_sets = {value:key for key, value in char_sets.items()}

char_vals = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_vals = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
#print(json.dumps(char_sets, indent=4))



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
    incomplete_lines.append((line, opened_stack))

error_chars = []


#<codecell>

'''Part 2'''

incomplete_lines = []

for i in input_list:
    find_errors(i)

result1 = sum([char_vals[i] for i in error_chars])

print(f'{result1=}')

scores = []

incomplete_lines

for i in incomplete_lines:
    completion_chars = [reverse_char_sets[x] for x in i[1][::-1]]
    print(completion_chars)
    score = 0
    for x in completion_chars:
        score = (score * 5) + completion_vals[x]
    scores.append(score)

scores

result2 = sorted(scores)[int((len(scores)-1)/2)]

print(f'{result2=}')


#<codecell>

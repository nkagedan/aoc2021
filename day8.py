#<codecell>
'''Setup'''

import pandas as pd
import numpy as np
import pprint
pp = pprint.PrettyPrinter(indent=4)

file = 'input8.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
#input_list = [int(i) for i in data.split(',')]
#df = pd.DataFrame(input_list, columns =['raw_input'])

#<codecell>

'''Part 1'''

unique_char_counts = [2, 4, 3, 7]

count = 0

for i in input_list:
    output_chars = i.split('|')[1].strip().split()
    for x in output_chars:
        if len(x) in unique_char_counts:
            count += 1

print(f'part 1 result = {count}')

#<codecell>

'''Part 2'''

def find_output_value(entry):

    digit_key = {}
    decoder_digits = entry.split('|')[0].strip().split()
    digit_key[1] = [list(sorted(i)) for i in decoder_digits if len(i) == 2][0]
    digit_key[4] = [list(sorted(i)) for i in decoder_digits if len(i) == 4][0]
    digit_key[7] = [list(sorted(i)) for i in decoder_digits if len(i) == 3][0]
    digit_key[8] = [list(sorted(i)) for i in decoder_digits if len(i) == 7][0]
    digit_key[3] = [list(sorted(i)) for i in decoder_digits if len(i) == 5 and all(elem in list(i) for elem in digit_key[7])][0]
    digit_key[9] = list(sorted(''.join(set(digit_key[4]+digit_key[3]))))
    digit_key[0] = [list(sorted(i)) for i in decoder_digits if (len(i) == 6) and (all(elem in list(i) for elem in digit_key[1])) and (list(sorted(i)) not in digit_key.values())][0]
    digit_key[6] = [list(sorted(i)) for i in decoder_digits if len(i) == 6 and list(sorted(i)) not in digit_key.values()][0]
    digit_key[5] = [list(sorted(i)) for i in decoder_digits if len(i) == 5 and all(elem in digit_key[6] for elem in list(i))][0]
    digit_key[2] = [list(sorted(i)) for i in decoder_digits if len(i) == 5 and list(sorted(i)) not in digit_key.values()][0]

    output_digits = entry.split('|')[1].strip().split()

    output_numbers = []
    for i in output_digits:
        for key in range(0,10):
            if digit_key[key] == list(sorted(i)):
                output_numbers.append(key)

    result = int(''.join([str(i) for i in output_numbers]))

    pp.pprint(digit_key)
    print(output_digits)
    print(output_numbers)
    print(result)

    return result

final_result = sum([find_output_value(i) for i in input_list])

print(f'part 2 result = {final_result}')

#<codecell>

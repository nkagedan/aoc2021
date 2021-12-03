'''Load Input Data'''

import pandas as pd

file = 'input3.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
df = pd.DataFrame(input_list, columns =['raw_input'])


'''Part 1'''
print(len(input_list))

gamma = ''
epsilon = ''

for i in range(len(input_list[0])):
    count = 0
    for binary in input_list:
        count += int(binary[i])
    if count >= len(input_list)/2:
        gamma += '1'
    else:
        gamma += '0'

print(gamma)
gamma_decimal = int(gamma,2)
print(gamma_decimal)

for i in range(len(gamma)):
    epsilon += str(abs(int(gamma[i])-1))

print(epsilon)
epsilon_decimal = int(epsilon,2)
print(epsilon_decimal)

power_cons = gamma_decimal*epsilon_decimal

print(power_cons)

'''Part 2'''

# Oxygen

character = 0

while len(df) > 1:

    df['char_x'] = df['raw_input'].str[character]
    counts = df['char_x'].value_counts()
    counts
    if int(counts.loc['1']) >= int(counts.loc['0']):
        target = '1'
    else:
        target = '0'
    df = df.loc[df['char_x'] == target]

    len(df)

    character += 1
    if character > len(input_list[0]):
        character = 0
    character

oxygen_binary = df['raw_input'].values[0]
oxygen_binary
oxygen_decimal = int(oxygen_binary,2)
oxygen_decimal

# co2

df = pd.DataFrame(input_list, columns =['raw_input'])

character = 0

while len(df) > 1:

    df['char_x'] = df['raw_input'].str[character]
    counts = df['char_x'].value_counts()
    counts
    if int(counts.loc['0']) <= int(counts.loc['1']):
        target = '0'
    else:
        target = '1'
    df = df.loc[df['char_x'] == target]

    len(df)

    character += 1
    if character > len(input_list[0]):
        character = 0
    character

co2_binary = df['raw_input'].values[0]
co2_binary
co2_decimal = int(co2_binary,2)
co2_decimal

# result

life_support = oxygen_decimal*co2_decimal
life_support

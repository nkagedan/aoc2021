'''Part 1'''

file = 'input2.txt'

with open(file, 'r') as file:
    data = file.read().strip()

listed = data.splitlines()

pos = 0
depth = 0

for i in listed:
    val = int(i[-1])
    if i[0] == 'f':
        pos += val
    elif i[0] == 'd':
        depth += val
    else:
        depth -= val

result = pos * depth
print(f'{result=}')


'''Part 2'''

pos = 0
depth = 0
aim = 0

for i in listed:
    val = int(i[-1])
    if i[0] == 'f':
        pos += val
        depth += val*aim
    elif i[0] == 'd':
        aim += val
    else:
        aim -= val

result2 = pos * depth
print(f'{result2=}')

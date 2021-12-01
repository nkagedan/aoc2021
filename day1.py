path_prefix = 'C:\\Users\\nkage\\lpthw\\aoc2021\\'
file_name = 'input1.txt'
path = path_prefix + file_name

with open(path, 'r') as file:
    data = file.read().strip()

listed = data.splitlines()

len(listed)

count = 0

for i in range(len(listed)):
     if listed[i] > listed[i-1]:
          count += 1

print(count)

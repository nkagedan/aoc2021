'''Part 1'''

file = 'input1.txt'

with open(file, 'r') as file:
    data = file.read().strip()

listed = data.splitlines()
listed = [int(i) for i in listed]

count = 0

for i in range(len(listed)):
     if listed[i] > listed[i-1]:
          count += 1

print(count)

'''Part 2'''

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

sums = [sum(listed[i:i+3]) for i in range(len(listed))]

listed[1999:2001]

count = 0

for i in range(len(sums)):
     if sums[i] > sums[i-1]:
          count += 1

print(count)

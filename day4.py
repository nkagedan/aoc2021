'''Load Input Data'''

import pandas as pd

file = 'input4.txt'

with open(file, 'r') as file:
    data = file.read().strip()

input_list = data.splitlines()
df = pd.DataFrame(input_list, columns =['raw_input'])

'''Part 1'''

# Get numbers to be called

call_list = df['raw_input'][0].split(',')

df = df[2:].reset_index()

# Generate bingo boards

bingo_boards = []

counter = 0
for i in list(range(len(df)))[::6]:
    lists = [df.iloc[x]['raw_input'].split() for x in range(i,i+5)]
    bingo_boards.append(pd.DataFrame(lists))
    counter += 1

# Call numbers and find winning board

bingo_boards[0]

bingo_boards[0].iterrows()


for i in range(len(call_list)):
    current_call = call_list[:i+1]
    for board in bingo_boards:
        for x in range(0,5):
            if all(item in current_call for item in board.iloc[x].tolist() or ):
                winner = board
                break
            if all(item in current_call for item in board[x].tolist()):
                winner = board
                break

i
winner






'''Part 2'''

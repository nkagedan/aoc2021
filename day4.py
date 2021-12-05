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

def check_for_winners(numbers, boards):
    for i in range(len(numbers)):
        current_call = numbers[:i+1]
        for board in boards:
            for x in range(0,5):
                if (all(item in current_call for item in board.iloc[x].tolist())) or (all(item in current_call for item in board[x].tolist())):
                    return (board, current_call)


win_board, win_call = check_for_winners(call_list, bingo_boards)

win_num = int(win_call[-1])
unmarked = [int(i) for i in win_board.stack().tolist() if i not in win_call]
sum(unmarked) * win_num


'''Part 2'''

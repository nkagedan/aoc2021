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
df
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

series = pd.Series(bingo_boards)
boards_df = pd.DataFrame(series)

def calls_to_win(board):
    call_count = 1
    for i in range(len(call_list)):
        current_call = call_list[:i+1]
        for x in range(0,5):
            if (all(item in current_call for item in board.iloc[x].tolist())) or (all(item in current_call for item in board[x].tolist())):
                return call_count
        call_count +=1

boards_df['calls'] = boards_df[0].apply(calls_to_win)
boards_df.sort_values(by='calls', ascending=False, inplace=True)
loser_board = boards_df.iloc[0,0]
loser_calls = boards_df.iloc[0,1]
loser_call = int(call_list[loser_calls-1])
value_sum = sum([int(i) for i in loser_board.stack().tolist() if i not in call_list[:loser_calls]])
result = value_sum * loser_call
print(f'{result=}')

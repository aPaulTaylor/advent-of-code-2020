with open('input/day04-input.txt', 'r') as f:
    input = [x[:-1] for x in f.readlines()]

numbers=[int(x) for x in input[0].split(',')]

def parse_board_line(bl):
    return [int(bl[i:i+3]) for i in range(0,len(bl),3)]

boards = []
for i in range(2,len(input),6):
    boards.append([
        [parse_board_line(l) for l in input[i:i+5]],
        [[0]*5 for j in range(5)]])

def mark_number(board,num):
    matches = [[1 if board[0][i][j]==num else board[1][i][j] for j in range(5)] for i in range(5)]
    return [board[0], matches]

def board_wins(board):
    if any(all(x==1 for x in l) for l in board[1]):
        return True
    if any(all(x == 1 for x in [l[i] for l in board[1]]) for i in range(5)):
        return True
    return False

# Part 1
winner=False
number_list = numbers[::-1]
while not winner:
    call_num = number_list.pop()
    boards = [mark_number(b, call_num) for b in boards]
    win_list = [board_wins(b) for b in boards]
    winner = any(win_list)

winning_board=boards[win_list.index(True)]
board_sum = sum(sum(winning_board[0][i][j]*(1-winning_board[1][i][j]) for j in range(5)) for i in range(5))
print(board_sum * call_num)

# Part 2
winner=False
number_list = numbers[::-1]
while not winner:
    call_num = number_list.pop()
    boards = [mark_number(b, call_num) for b in boards]
    win_list = [board_wins(b) for b in boards]
    if len(win_list) - sum(win_list) == 1:
        last_winner = win_list.index(False)
    winner = all(win_list)

winning_board=boards[last_winner]
board_sum = sum(sum(winning_board[0][i][j]*(1-winning_board[1][i][j]) for j in range(5)) for i in range(5))
print(board_sum * call_num)
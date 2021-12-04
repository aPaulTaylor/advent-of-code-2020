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

def play_bingo(boards,number_list,criterion):
    winner=False
    while not winner:
        call_num = number_list.pop()
        boards = [mark_number(b, call_num) for b in boards]
        win_list = [board_wins(b) for b in boards]
        if criterion=='first':
            winner = any(win_list)
            if winner:
                win_num = win_list.index(True)
        else:
            if len(win_list) - sum(win_list) == 1:
                win_num = win_list.index(False)
            winner = all(win_list)
    winning_board=boards[win_num]
    board_sum = sum(sum(winning_board[0][i][j]*(1-winning_board[1][i][j]) for j in range(5)) for i in range(5))
    return(board_sum * call_num)

print(play_bingo(boards,numbers[::-1],'first')) # Part 1
print(play_bingo(boards,numbers[::-1],'last')) # Part 2

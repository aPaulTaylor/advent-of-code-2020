with open('c:/Users/paula/PycharmProjects/advent-of-code/day22-input.txt', 'r') as f:
    input = f.read()

p1 = [int(n) for n in input.split('\n\n')[0].split('\n')[1:]][::-1]
p2 = [int(n) for n in input.split('\n\n')[1].split('\n')[1:-1]][::-1]

# Part 1
while min(len(p1),len(p2))>0:
    p1_card = p1.pop()
    p2_card = p2.pop()
    if p1_card > p2_card:
        p1 = [p2_card, p1_card] + p1
    else:
        p2 = [p1_card, p2_card] + p2

print(sum((i+1)*n for i,n in enumerate(p1)))

# Part 2

p1 = [int(n) for n in input.split('\n\n')[0].split('\n')[1:]][::-1]
p2 = [int(n) for n in input.split('\n\n')[1].split('\n')[1:-1]][::-1]

'''
- Before either player deals a card, if there was a previous round in this game that had exactly the same cards in the
same order in the same players' decks, the game instantly ends in a win for player 1. Previous rounds from other games
are not considered. (This prevents infinite games of Recursive Combat, which everyone agrees is a bad idea.)
- Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the top
card of their deck as normal.
- If both players have at least as many cards remaining in their deck as the value of the card they just drew, the
winner of the round is determined by playing a new game of Recursive Combat (see below).
- Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner of the round
is the player with the higher-value card.
'''

def play_recursive_game(p1_nums,p2_nums):
    prev_round_states = []
    winner=0
    while winner==0:
        if ','.join([str(n) for n in p1_nums])+'-'+','.join([str(n) for n in p2_nums]) in prev_round_states:
            #print('prev state')
            winner = 1
        elif min(len(p1_nums),len(p2_nums))==0:
            #print('empty pile')
            if len(p1_nums)==0:
                winner=2
            else:
                winner=1
        else:
            prev_round_states.append(','.join([str(n) for n in p1_nums]) + '-' + ','.join([str(n) for n in p2_nums]))
            #print(prev_round_states[-1])
            p1_card = p1_nums.pop()
            p2_card = p2_nums.pop()
            if (p1_card <= len(p1_nums) and p2_card <= len(p2_nums)):
                #print('subgame')
                subgame_winner = play_recursive_game(p1_nums[:],p2_nums[:])[0]
                if subgame_winner == 1:
                    p1_nums = [p2_card,p1_card] + p1_nums
                else:
                    p2_nums = [p1_card, p2_card] + p2_nums
            else:
                #print('faceoff')
                if p1_card > p2_card:
                    p1_nums = [p2_card,p1_card] + p1_nums
                else:
                    p2_nums = [p1_card, p2_card] + p2_nums
    return [winner, p1_nums, p2_nums]

results=play_recursive_game([19,43],[14,29,2])
print(results)
results=play_recursive_game([1,3,6,2,9],[10,7,4,8,5])
print(results)
results=play_recursive_game(p1,p2)
print(results)
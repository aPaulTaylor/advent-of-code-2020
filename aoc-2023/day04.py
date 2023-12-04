with open('input/day04-input.txt', 'r') as f:
    cards_raw = [x.strip() for x in f.readlines()]

def parse_card(card_str):
    card_nums=card_str.split(':')[1].split('|')
    win_nums=[int(card_nums[0][i:i+3]) for i in range(0,len(card_nums[0])-1,3)]
    have_nums = [int(card_nums[1][i:i + 3]) for i in range(0, len(card_nums[1]), 3)]
    return [win_nums, have_nums]

cards = [parse_card(cr) for cr in cards_raw]

total_pts=0
for card in cards:
    matches=[n for n in card[0] if n in card[1]]
    if len(matches)>0:
        total_pts += 2**(len(matches)-1)

print(total_pts)

card_counts=[1]*len(cards)
for i in range(len(cards)):
    num_matches = sum(1 for n in cards[i][0] if n in cards[i][1])
    for j in range(1,num_matches+1):
        card_counts[i+j]+=card_counts[i]

print(sum(card_counts))
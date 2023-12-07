with open('input/day07-input.txt', 'r') as f:
    hands_raw = [x.strip() for x in f.readlines()]

hands=[ {'bid':int(x.split(' ')[1]), 'hand':x.split(' ')[0]} for x in hands_raw ]

RANK_SCORES={'A':14,'K':13,'Q':12,'J':11,'T':10}
for i in range(2,10):
    RANK_SCORES[str(i)]=i

def score_hand(hand):
    dist_ranks=len(set(hand))
    num_pairs=sum(1 for r in RANK_SCORES.keys() if hand.count(r)==2 )
    if dist_ranks==1:
        hand_score=70000000000 #5ofakind
    if dist_ranks==2:
        if num_pairs==0:
            hand_score=60000000000 #4ofakind
        else:
            hand_score=50000000000 #fullhouse
    if dist_ranks==3:
        if num_pairs==0:
            hand_score=40000000000 #threeofakind
        else:
            hand_score=30000000000 #twopair
    if dist_ranks==4:
        hand_score=20000000000 #onepair
    if dist_ranks==5:
        hand_score=10000000000 #highcard
    for i in range(5):
        hand_score += RANK_SCORES[hand[i]]*(100**(4-i))
    return hand_score

hands.sort( key=lambda x:score_hand(x['hand']) )

total_score=0
for i in range(len(hands)):
    total_score += hands[i]['bid']*(i+1)

print(total_score)

RANK_SCORES['J']=1
def score_hand_j(hand_in):
    best_rank_score=0
    for jrank in 'AKQT98765432':
        hand=hand_in.replace('J',jrank)
        dist_ranks=len(set(hand))
        num_pairs=sum(1 for r in RANK_SCORES.keys() if hand.count(r)==2 )
        if dist_ranks==1:
            hand_score=70000000000 #5ofakind
        if dist_ranks==2:
            if num_pairs==0:
                hand_score=60000000000 #4ofakind
            else:
                hand_score=50000000000 #fullhouse
        if dist_ranks==3:
            if num_pairs==0:
                hand_score=40000000000 #threeofakind
            else:
                hand_score=30000000000 #twopair
        if dist_ranks==4:
            hand_score=20000000000 #onepair
        if dist_ranks==5:
            hand_score=10000000000 #highcard
        if hand_score>best_rank_score:
            best_rank_score=hand_score
    hand_score=best_rank_score
    for i in range(5):
        hand_score += RANK_SCORES[hand_in[i]]*(100**(4-i))
    return hand_score

hands.sort( key=lambda x:score_hand_j(x['hand']) )

total_score=0
for i in range(len(hands)):
    total_score += hands[i]['bid']*(i+1)

print(total_score)
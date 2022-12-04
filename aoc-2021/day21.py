# Player 1 starting position: 7
# Player 2 starting position: 2

scores=[0,0]
positions=[7,2]
die_val=1
cur_player = 0
while max(scores)<1000:
    roll=(die_val*3)+3
    die_val+=3
    positions[cur_player]+=roll
    while positions[cur_player]>10:
        positions[cur_player] -= 10
    scores[cur_player]+=positions[cur_player]
    cur_player=1-cur_player
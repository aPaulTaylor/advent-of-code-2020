with open('input/day02-input.txt', 'r') as f:
    games_raw = [x.strip() for x in f.readlines()]


def parse_game(game_raw):
    game_draws_raw = game_raw.split(':')[1].split(';')
    game_draws=[]
    for gdr in game_draws_raw:
        gd={}
        for x in gdr.split(','):
            gd[x.strip().split(' ')[1]] = int(x.strip().split(' ')[0])
        game_draws.append(gd)
    return game_draws


games = [parse_game(gr) for gr in games_raw]

def check_draw(draw, criteria):
    return all(draw[col]<=criteria[col] for col in draw)

def check_game(game, criteria):
    return all(check_draw(draw, criteria) for draw in game)

tot_ids=0
for i,game in enumerate(games):
    if check_game(game,{'red':12,'green':13,'blue':14}):
        tot_ids += i+1
print(tot_ids)


def calculate_power(game):
    power=1
    for col in ['red','green','blue']:
        min_cubes=0
        for draw in game:
            if col in draw:
                min_cubes=max([min_cubes, draw[col]])
        power = power*min_cubes
    return power

print(sum(calculate_power(game) for game in games))

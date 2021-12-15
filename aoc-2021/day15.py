with open('input/day15-input.txt', 'r') as f:
    risk = [[int(n) for n in x[:-1]] for x in f.readlines()]

dim=100
big_risk=[]
for r in range(500):
    row=[]
    for c in range(500):
        new_risk = (risk[r % 100][c % 100] + r//100 + c//100) % 9
        row.append(9 if new_risk==0 else new_risk )
    big_risk.append(row)

risk=big_risk ### comment out these lines to run part 1
dim=500       ### comment out these lines to run part 1

def adj_coords(coord):
    i=coord[0]
    j=coord[1]
    adj_coords=[(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    adj_coords=[c for c in adj_coords if 0 <= c[0] < dim and 0 <= c[1] < dim]
    return adj_coords

distances=[[0 for i in range(dim)] for j in range(dim)]

for d in range(1,(2*dim)-1):
    for i in range(max(0,d-(dim-1)),min(dim,d+1)):
        j=d-i
        if i==0:
            distances[i][j] = distances[i][j-1] + risk[i][j]
        elif j==0:
            distances[i][j] = distances[i-1][j] + risk[i][j]
        else:
            distances[i][j] = min(distances[i-1][j],distances[i][j-1]) + risk[i][j]

def refine_distances(risk,distances):
    new_best = [[0 for i in range(dim)] for j in range(dim)]
    for i in range(dim):
        for j in range(dim):
            adjs=adj_coords((i,j))
            best_dist = min(distances[c[0]][c[1]] for c in adjs) + risk[i][j]
            new_best[i][j] = min(best_dist,distances[i][j])
    return new_best

better_found=True
while better_found:
    better_found=False
    new_dists = refine_distances(risk, distances)
    if sum(sum(dl) for dl in new_dists) < sum(sum(dl) for dl in distances):
        better_found=True
        distances = new_dists

print(distances[-1][-1])

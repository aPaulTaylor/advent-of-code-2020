with open('input/day05-input.txt', 'r') as f:
    input = [x.strip() for x in f.readlines()]

lines_coords = [[list(map(int,x.split(','))) for x in l.split(' -> ')] for l in input]

def incl_range(x,y):
    return list(range(x,y+1)) if y>=x else list(range(y,x+1))[::-1]

def find_danger_squares(lines_coords,diags):
    floor_map = [[0 for x in range(1000)] for y in range(1000)]
    for lc in lines_coords:
        if lc[0][0]==lc[1][0]:
            for i in incl_range(lc[0][1],lc[1][1]):
                floor_map[lc[0][0]][i]+=1
        elif lc[0][1]==lc[1][1]:
            for i in incl_range(lc[0][0],lc[1][0]):
                floor_map[i][lc[0][1]]+=1
        else:
            if diags:
                xrange = incl_range(lc[0][0],lc[1][0])
                yrange = incl_range(lc[0][1],lc[1][1])
                for i in range(len(xrange)):
                    floor_map[xrange[i]][yrange[i]]+=1
    return sum(sum(1 if x>1 else 0 for x in fl) for fl in floor_map)

print(find_danger_squares(lines_coords,False))
print(find_danger_squares(lines_coords,True))

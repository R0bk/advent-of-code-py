inp = open('../input/1.txt', 'r').read().split(', ')
positions = set()
tp = []
direc, pos, trans = (0, [0, 0], {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]})
for x in inp:
    direc = (direc + 1) % 4 if x[0] == 'L' else (direc - 1) % 4
    for j in range(int(x[1:])):
        pos = [e + (trans[direc][i]) for i, e in enumerate(pos)]
        if tuple(pos) in positions:
            tp.append(pos)
        positions.add(tuple(pos))
dists = ([sum([abs(i) for i in x]) for x in tp], sum([abs(i) for i in pos]))
print(dists)

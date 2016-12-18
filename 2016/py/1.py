inp = open('../input/1.txt', 'r').read().split(', ')
direc, pos, trans = (0, [0, 0], {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]})
for x in inp:
    direc = (direc + 1) % 4 if x[0] == 'L' else (direc - 1) % 4
    pos = [e + (trans[direc][i] * int(x[1:])) for i, e in enumerate(pos)]
dists = (sum([i**2 for i in pos])**0.5, sum([abs(i) for i in pos]))
print(dists)

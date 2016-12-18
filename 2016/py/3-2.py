inp = open('../input/3.txt', 'r').readlines()
poss, imposs, cinp = ([], [], [])
[cinp.extend(x) for x in list(map(list, zip(*[y.split() for y in inp])))]
for t in [cinp[i * 3:i * 3 + 3] for i in range(int(len(cinp) / 3))]:
    vals = list(map(int, t))
    vals.sort()
    imposs.append(vals) if vals[-1] >= sum(vals[:-1]) else poss.append(vals)
print(len(poss), len(imposs), len(inp))

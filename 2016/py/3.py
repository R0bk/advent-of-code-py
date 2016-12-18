inp = open('../input/3.txt', 'r').readlines()
poss, imposs = ([], [])
for t in inp:
    vals = list(map(int, t.split()))
    vals.sort()
    imposs.append(vals) if vals[-1] >= sum(vals[:-1]) else poss.append(vals)
print(len(poss), len(imposs), len(inp))
print(imposs, poss)

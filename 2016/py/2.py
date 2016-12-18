inp = open('../input/2.txt', 'r').read().split()
keys, pos_1, tran = ([], [0, 0], {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]})
key2num = {(-1, 1): 1,
           (0, 1): 2,
           (1, 1): 3,
           (-1, 0): 4,
           (0, 0): 5,
           (1, 0): 6,
           (-1, -1): 7,
           (0, -1): 8,
           (1, -1): 9}
for l in inp:
    for c in l:
        pos_2 = [x + tran[c][i] for i, x in enumerate(pos_1)]
        if not any([abs(i) - 1 for i in pos_2 if i != 0]):
            pos_1 = [x + tran[c][i] for i, x in enumerate(pos_1)]
    keys.append(key2num[tuple(pos_1)])
print(''.join(map(lambda x: str(x), keys)))
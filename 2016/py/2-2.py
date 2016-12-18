inp = open('../input/2.txt', 'r').read().split()
keys, pos_1, tran = ([], [-2, 0], {'U': [0, 1], 'D': [0, -1], 'L': [-1, 0], 'R': [1, 0]})

key2num = {(0, 2): 1,
           (-1, 1): 2,
           (0, 1): 3,
           (1, 1): 4,
           (-2, 0): 5,
           (-1, 0): 6,
           (0, 0): 7,
           (1, 0): 8,
           (2, 0): 9,
           (-1, -1): 'A',
           (0, -1): 'B',
           (1, -1): 'C',
           (0, -2): 'D'}
for l in inp:
    for c in l:
        pos_2 = [x + tran[c][i] for i, x in enumerate(pos_1)]
        if not sum([abs(i) for i in pos_2]) > 2:
            pos_1 = [x + tran[c][i] for i, x in enumerate(pos_1)]
    keys.append(key2num[tuple(pos_1)])
print(''.join(map(lambda x: str(x), keys)))

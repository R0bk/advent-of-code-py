import collections
inp = open('../input/4.txt', 'r').readlines()
corr, incorr, c = ([], [], [])
for l in inp:
    c = collections.Counter(l.split('[')[0].replace('-', ''))
    c = ''.join([y[0] for y in [x for x in sorted(
        c.most_common(), key=lambda x: (-x[1], x[0])) if x[0].isalpha()][:5]])
    corr.append(l) if c == l.split('[')[-1][:-2] else incorr.append(l)
print(corr, sum([int(x.split('[')[0].split('-')[-1]) for x in corr]))

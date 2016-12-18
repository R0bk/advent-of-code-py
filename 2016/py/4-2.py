import collections
inp, corr = open('../input/4.txt', 'r').readlines(), []
corr = [l for l in inp if l.split('[')[-1][:-2] == ''.join([y[0] for y in [
    x for x in sorted(collections.Counter(l.split('[')[0].replace('-', ''))
        .most_common(), key=lambda x: (-x[1], x[0])) if x[0].isalpha()][:5]])]
print([z for z in [''.join([chr((((ord(y) & 0b11111) + int(x.split('[')[0][-3:
    ]) - 1) % 26) + 97) for y in x.split('[')[0].replace('-', '')] + [x.split(
        '[')[0][-3:]]) for x in corr] if z.find('north') + 1])

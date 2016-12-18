import hashlib
inp, n, s = open('../input/5.txt', 'r').read(), [], [0] * 10
has = lambda x: hashlib.md5((inp + str(x)).encode()).hexdigest()
[n.append(has(x)[5:7]) for x in range(30000000) if (
    has(x)[:5] == '00000') and has(x)[5].isdigit()]
for x in n:
    if not s[int(x[0])]:
        s[int(x[0])] = x[1]
print(''.join(map(str, s))[:8])

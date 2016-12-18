import hashlib
inp = open('../input/5.txt', 'r').read()
print(''.join([hashlib.md5((inp + str(x)).encode()).hexdigest()[5]
               for x in range(10000000) if (hashlib.md5((inp + str(x)).
                    encode()).hexdigest()[:5] == '00000')])[:8])


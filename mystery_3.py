line = 'a' * 30000
filename = '/tmp/fake.txt'

with open(filename, 'w') as f:
    for i in xrange(10000):
        f.write(line)


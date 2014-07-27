from itertools import dropwhile
with open('test.txt') as f:
    for line in dropwhile(lambda f : f.startswith('#'), f):
        print line...
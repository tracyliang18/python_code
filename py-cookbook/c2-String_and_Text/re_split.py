import re
f = open('test.txt')
for line in f:
    print line
    print re.split(r'[;,\s]\s*', line)
    print re.split(r'[;,\s]*', line)

print re.split(r'\W+', 'Words, words, words.')
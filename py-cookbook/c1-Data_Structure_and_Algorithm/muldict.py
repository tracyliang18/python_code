from collections import defaultdict

d= defaultdict(list)
d['a'].append(1)
d['b'].append(2)

print(d)

s={}
s.setdefault('a',[]).append(1)
s.setdefault('a',{}).append((1,1))
print(s)

pairs={}
for key,value in pairs:
    if key not in d:
        d[key]=[]
    d[key].append(value)
from collections import OrderedDict
import json
d = OrderedDict()
d['a']=1
d['2']=2

for item in d:
    print(item)
for item in d.__reversed__():
    print(item)




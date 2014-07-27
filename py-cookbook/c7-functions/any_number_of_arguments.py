from __future__ import division
def avg(first, *rest):
    return (first + sum(rest))/(1+len(rest))

print avg(1)
print avg(1,2,3,4)

#import html
def make_element(name, value, **attr):
    #key = ['%s = "%s"' % item for item in attr.items()]
    akey = ['%s = "%s"' % (key, v) for key,v in attr.items() ]

    print akey

make_element("haha",1,sex='male',height=176)

d = {1:2,3:4}
print d[1]
for k,v in d.items():
    print k,v
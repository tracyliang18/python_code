a = [1,2,3,4,5,6,7,7,8]

def dedup(a, key=None):
    seen = set()
    for i in a:
        if i not in seen:
            yield i
        seen.add(i)

dedup(a)
c = (dedup(a))
#print d= list(c)
print d


#
from collections import deque
a = deque([1,2,3])

a.append(9)
a.appendleft(0)
a.append(3)
print(a.count(3))
#a.clear()
#print(len(a))

a.extend("adfadsf")



a.popleft()
a.pop()
a.remove('a')
a.reverse()
print(a)
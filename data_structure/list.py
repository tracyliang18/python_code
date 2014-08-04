#append O(1)
a = []
a[len(a):] = [10]
a.append(20)
print a

#extend O(k), k is length of list for extention
a.extend([1,2,3])
print a

#O(n)
print max(a)
print min(b)
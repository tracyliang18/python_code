a = {
    'x':1,
    'y':2,
    'z':3
}

b= {
    'w':10,
    'x':11,
    'y':2
}

print set(a.keys()) & set(b.keys())
print set(a.items()) & set(b.items())

#c = {key:a[key] for key in a.keys() - ['x','y']}

a = list((1,2,1,2,3))
print a.count(1)

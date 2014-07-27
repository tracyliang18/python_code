with open('test.txt') as f:
    try:
        while True:
            line = next(f)
            print(line)
    except StopIteration:
        pass

items = [1,2,3]
it = iter(items) #init a iterator by list
print next(it)

for i in [1,2,3]:
    print i
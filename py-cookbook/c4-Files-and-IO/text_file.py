with open('test.txt', 'rt') as f:
    data = f.read()
    with open('test2.txt','wt') as out:
        out.write(data)

#redirect print
f = open('haha.txt',"wt")
print("haha",file=f)
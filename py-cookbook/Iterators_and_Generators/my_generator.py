def frange(start, stop, increment):
    while(start <= stop):
        yield start
        start += increment
    print "wakaka"


for i in frange(1,10,1):
    print i
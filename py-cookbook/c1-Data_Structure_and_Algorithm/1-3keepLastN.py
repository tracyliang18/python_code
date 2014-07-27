from collections import deque
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)
 
 
if __name__ == '__main__':
    with open('test.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end=' ')
            print(line, end = ' ')
            print('-'*20)        


# l = [1,2,3]
# for i in l:
#     l.append(i)
#     print(i)                                              

# 
# mygenerator = (x*x for x in range(3))
# print(mygenerator)
# for i in mygenerator:
#     print(i)
#     
# for i in mygenerator:
#     print(i)
#     
# for i in mygenerator:
#     print(i)
# def drop_last_first(grades):
#     first, *middle, last = grades
#     return avg(middle)
record = ('liangjiajun', '642098212@qq.com', "18771039360", "076022123464")
name, email, *phone = record
print(phone)


records = [
           ('foo', 1, 2),
           ('bar',11),
           ('foo',3,4)]

def do_foo(a,b):
    print(a,b)

def do_bar(c):
    print(c)

for type, *args in records:
    if type == 'foo':
        print(*args) #the *args unpack is required
        do_foo(args)
    if type == 'bar':
        do_bar(*args)
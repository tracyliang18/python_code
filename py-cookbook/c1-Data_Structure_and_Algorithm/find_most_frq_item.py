__author__ = 'tracyliang'
# def most_fre_item(l):
#     m = {}
#     for item in l:
#         if item not in m.keys():
#             m[item] = 1
#         else:
#             m[item] += 1

class A(object):
    def __init__(self, name):
        self.__name = name
    def __hash__(self):
        return int(self.__name)
    def __repr__(self):
        return "item%s" %  (self.__name)


lst = [A(str(i)) for i in [1,1,2,3,4]]


from collections import Counter
c = Counter(lst)
print c

c2 = Counter([1,2,3,1,2,3])
print c2



# def minnum(*values,clip=None):
#     m = min(values)
#     if clip is not None:
#         m = clip if clip > m else m
#     print clip,m
#     return m
#
# print minnum(1,2,3,45)
# #print minnum(clip=2)

# def recv(maxsize, *, block):
#     print maxsize,block
#
# recv(10,block=False)

def haha(v1,v2,block=None):
    print v1,v2,block

haha(1,2)
haha(1,2,block="haha")

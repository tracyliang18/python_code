import sys
def main():
    m=0

    fun1()

def fun1():
    f1=1
    fun2()

def fun2():
    f2=2
    def haha():
        pass
    a=hahaha()


class hahaha:
    def __init__(self):
        print sys._getframe(2).f_locals

main()



class Person:
    def __init__(self,name):
        self.name = name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("expected string")
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("can't be deleted")

    def haha(self):
        pass


tom = Person("tom")
print tom.__dict__
print tom.name

import math
class Circle:
    def __init__(self,r):
        self.r = r
    @property
    def area(self):
        return math.pi * self.r ** 2
    @property
    def primeter(self):
        return 2 * math.pi * self.r

    @primeter.getter
    def primeter(self):
        return "getter"

    @primeter.setter
    def primeter(self, value):
        print "setting"
        raise AttributeError("cao")

    def aprint(self):
        print self.r
        print self.area
        print self.primeter


c = Circle(3)
c.aprint()
print getattr(c,"primeter")
print c.__getattr__
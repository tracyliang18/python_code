#super only works for new-type class
class A(object):
    def spam(self):
        print "A.spam"

class B(A):
    def spam(self):
        print "B.spam"
        super(B,self).spam()

#super is usually used for all parent's overrided method,
#in other's word, deried class override the parent's method to do more work



b = B()
b.spam()
print B.__mro__

class Person(object):
    a="hh"
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        if not isinstance(value, str):
            raise TypeError
        self._name = value
    @name.deleter
    def name(self):
        raise AttributeError

class SubPerson(Person):
    @Person.name.setter
    def name(self,value):
        print "setting"
        super(SubPerson,SubPerson).name.__set__(self,value)

sp = SubPerson("haha")
print Person.__dict__

class A(object):
    def foo():
        print 'I am foo'
    def foo2(cls):
        print 'I am foo2', cls
    def foo3(self):
        print 'I am foo3', self
    foo=staticmethod(foo)
    foo2=classmethod(foo2)
a = A()
a.foo()
a.foo2()
A.foo2()
a.foo3()

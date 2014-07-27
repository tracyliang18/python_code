def change(x,y):
    x += 1
    y += 1

x=10
y=12
change(x,y)
print x,y

class PassByReference:
    def __init__(self):
        self.variable = 'Original'
        self.Change(self.variable)
        print self.variable

    def Change(self, var):
        var = 'Changed'

o = PassByReference()
print o.variable
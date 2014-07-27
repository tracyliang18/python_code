#define the __str__ and __repr__
class pair:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __repr__(self):
        return 'Pair({0.x!r},{0.y!r})'.format(self)
        #return 'Pair({%r}, {%r}) % (self.x, self.y))
    def __str__(self):
        return '({0.x!r},{0.y!r})'.format(self)
from decimal import Decimal
from decimal import localcontext
a = Decimal('1.1')
b = Decimal('1.3')
print "the result is {:0.8f}".format(a+b)

with localcontext() as ctx:
    ctx.prec= 4
    print a/b
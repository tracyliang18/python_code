#define __format__ function
_format = {
    'ymd' : '{d.year}-{d.month}-{d.day}',
    'mdy' : '{d.month}-{d.day}-{d.year}',
    'dmy' : '{d.day}-{d.month}-{d.year}'
}
class Date:
    def __init__(self, y, m, d):
        self.year = y
        self.month = m
        self.day = d

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _format[code]
        return fmt.format(d=self)

#print '{:haha} and {:kaka}'.format({"haha":"shit","kaka":"asfasd"})

print format(Date(2014,07,25))
print 'the date is {:ymd}'.format(Date(2014,07,25))
print 'the date is {ymd}, {ymd}'.format(ymd="haha")

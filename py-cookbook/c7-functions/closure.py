#sometime a single method class could have a better implement choice

#that is function closure

from urllib import urlopen

class UrlTemplate:
    def __init__(self, template):
        self.template = template
    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))

yahoo = UrlTemplate("http://finance.yahoo.com/d/quotes.csv?s={name}&f={fields}")
for line in yahoo.open(names='IBM,AAPL,FB',fields='sl1c1v'):
    print(line.decode('utf-8'))

def urltemplate(template):
    def open(**kwargs):
        return urlopen(template.format_map(kwargs))
    return open
import re

text1 = 'Today is 07/07/2014 and tomorrow is 07/08/2014'
m = re.compile('(\d+)/(\d+)/(\d+)')
print m
print m.findall(text1)

a = m.match('11/22/2222')
print a
print a
print a.group(1)
print a.groups()
import os
file = os.listdir('.')
print file
print any([f for f in file if f.endswith('.py')])
x=[f for f in file if f.endswith('.py')]
print any(f.endswith('.sdfpy') for f in file )

a = "afads"
print a.startswith('a')

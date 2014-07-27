#simple replace
s = 'hello, my name is liangjiajun'

print s.replace('liangjiajun','limeilan')
print s

#pattern replace , using re.sub
#such as replace date from 07/09/2014 to 2014-07-09

text = 'Today is 07/09/2014 and tommorow is 07/10/2014'
import re
text_re = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print text_re
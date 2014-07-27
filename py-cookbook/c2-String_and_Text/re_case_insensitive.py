#re has flags=re.IGNORECASE

import re
text = 'UPPER PYTHON, lower python, Mixed Python'
print re.findall('python',text,flags=re.IGNORECASE)
print re.sub('python','snake',text,re.IGNORECASE)

#the last re.sub has limitation, the second para of re.sub can be a function
#define a closure
def matchcase(word):
    def replace(m):
        print m
        text = m.group()
        print text
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

print re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)

from operator import itemgetter

rows = [
    {'fname' : 'Brain', 'lname' : 'Jones', 'uid' : 1003},
    {'fname' : 'David', 'lname' : 'Beazley', 'uid' : 1002},
    {'fname' : 'John', 'Cleese' : 'Jones', 'uid' : 1002},
    {'fname' : 'Big', 'Jones' : 'Jones', 'uid' : 1004},

]

print (sorted(rows, key = itemgetter('uid','fname')) == sorted(rows, key = lambda r: (r['uid'], r['fname'])))
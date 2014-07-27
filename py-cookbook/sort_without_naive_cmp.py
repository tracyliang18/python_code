from operator import attrgetter
__author__ = 'tracyliang'
class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)


lst = [User(i) for i in [1,4,6,3,9,5]]
print sorted(lst, key = attrgetter('user_id'))
print sorted(lst, key = lambda r : r.user_id)
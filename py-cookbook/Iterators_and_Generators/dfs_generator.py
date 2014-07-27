from collections import deque
class Node:
    def __init__(self, value):
        self._value = value
        self._children = []
    def __repr__(self):
        return 'Node{}'.format(self._value)

    def add_child(self,child):
        self._children.append(child)

    def __iter__(self):
        return iter(self._children)

    # def dfs(self):
    #     yield self
    #     for c in self:
    #         yield from c.dfs()

    def bfs(self):
        q = deque()
        q.append(self)
        while len(q) > 0:
            cur = q.popleft()
            yield cur
            for c in cur:
                q.append(c)



if __name__ == '__main__':
    root = Node(0)
    c1 = Node(1)
    c2 = Node(2)
    c3 = Node(3)
    root.add_child(c1)
    root.add_child(c2)
    c1.add_child(c3)

    for ch in root.bfs():
        print ch
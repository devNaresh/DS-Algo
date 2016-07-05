__author__ = 'naresh'

""" Refer below link for further assistence

https://www.hackerearth.com/notes/disjoint-set-union-union-find/

"""


class DisjointSet:
    def __init__(self, n):
        self.arr = [x for x in range(n)]
        self.size = None

    @classmethod
    def size_init(cls, n):
        obj = cls(n)
        obj.size = [1 for x in range(n)]
        return obj

    def find(self, n):
        if self.arr[n] == n:
            return n
        else:
            return self.find(self.arr[n])

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        else:
            self.arr[root1] = root2

    def unionSize(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return
        elif self.size[root1] < self.size[root2]:
            self.arr[root1] = self.arr[root2]
            self.size[root2] += self.size[root1]
        else:
            self.arr[root2] = self.arr[root1]
            self.size[root1] += self.size[root2]


if __name__ == '__main__':
    dsu = DisjointSet(6)
    dsu.union(1, 0)
    dsu.union(0, 2)
    dsu.union(3, 4)
    dsu.union(1, 4)
    print dsu.arr
    print '\n'
    dsu1 = DisjointSet.size_init(6)
    dsu1.unionSize(0, 1)
    dsu1.unionSize(1, 2)
    dsu1.unionSize(3, 2)
    print dsu1.arr
    print dsu1.size

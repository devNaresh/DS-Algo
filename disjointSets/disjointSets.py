__author__ = 'naresh'

"""
Refer below link for further assistence

https://www.youtube.com/watch?v=ID00PMy0-vE

"""


class Node:
    def __init__(self, data=None):
        self.rank = 0
        self.parent = None
        self.data = data

    def __eq__(self, other):
        return self.data == other.data

    def __str__(self):
        return str(self.parent.data)


class DisjointSet(object):
    def __init__(self):
        self.set_dic = {}

    @property
    def set_dic(self):
        return self.__set_dic

    @set_dic.setter
    def set_dic(self, value):
        self.__set_dic = value

    def make_set(self, data):
        node = Node(data)
        node.parent = node
        self.set_dic[data] = node

    def find_set(self, data):
        node = self.set_dic[data]
        if node.parent == node:
            return node
        else:
            node.parent = self.find_set(node.parent.data)
        return node.parent

    def union(self, data1, data2):
        node1 = self.find_set(data1)
        node2 = self.find_set(data2)

        if node1 == node2:
            return
        elif node1.rank >= node2.rank:
            node2.parent = node1
            if node1.rank == node2.rank:
                node1.rank += 1
        elif node1.rank < node2.rank:
            node1.parent = node2


if __name__ == '__main__':
    ds = DisjointSet()
    ds.make_set(1)
    ds.make_set(2)
    ds.make_set(3)
    ds.make_set(4)
    ds.make_set(5)
    ds.make_set(6)
    ds.make_set(7)

    ds.union(1, 2)
    ds.union(2, 3)
    ds.union(4, 5)
    ds.union(6, 7)
    ds.union(5, 6)
    ds.union(3, 7)

    print ds.find_set(1)
    print ds.find_set(2)
    print ds.find_set(3)
    print ds.find_set(4)
    print ds.find_set(5)
    print ds.find_set(6)
    print ds.find_set(7)

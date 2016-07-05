__author__ = 'naresh'

from linkLists.single_linked_list import Node


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enQueue(self, data):
        temp = Node(data)
        if self.rear is None:
            self.rear = self.front = temp
        else:
            self.rear.set_next(temp)
            self.rear = self.rear.get_next()

    def deQueue(self):
        if self.front is None:
            print "Queue is Empty"
        data = self.front.get_data()
        if self.front is self.rear:
            self.rear = None
        self.front = self.front.get_next()
        return data

    def frontData(self):
        if self.front is not None:
            return self.front.get_data()
        else:
            print "Queue is Empty"

    def rearData(self):
        if self.rear is not None:
            return self.rear.get_data()
        else:
            print "Queue is Empty"

    def isEmpty(self):
        return self.rear is None


if __name__ == '__main__':
    que = Queue()
    for x in range(0, 10):
        que.enQueue(x)

    while not que.isEmpty():
        print que.deQueue()

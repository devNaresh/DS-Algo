__author__ = 'naresh'

""" Refer below link for further assistence

https://www.hackerearth.com/notes/heaps-and-priority-queues/

"""


# TODO -: Implement with linklist
class Heap(object):
    # a.k.s percolateDown of Heap
    def max_heapify(self, arr, i, length):
        if len(arr) == 0:
            return
        else:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < length and arr[left] > arr[i]:
                largest = left
            if right < length and arr[right] > arr[largest]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                self.max_heapify(arr, largest, length)

    # a.k.s percolateUp of Heap
    def min_heapify(self, arr, i, length):
        if len(arr) == 0:
            return
        else:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < length and arr[left] < arr[i]:
                smallest = left
            if right < length and arr[right] < arr[smallest]:
                smallest = right
            if smallest != i:
                arr[i], arr[smallest] = arr[smallest], arr[i]
                self.min_heapify(arr, smallest, length)

    def build_max_heapify(self, arr):
        for i in reversed(xrange(len(arr) / 2)):
            self.max_heapify(arr, i, len(arr))

    def build_min_heapify(self, arr):
        for i in reversed(xrange(len(arr) / 2)):
            self.min_heapify(arr, i, len(arr))

    def heap_short(self, arr):
        length = len(arr)
        self.build_max_heapify(arr)
        for i in reversed(xrange(length)):
            arr[0], arr[i] = arr[i], arr[0]
            length -= 1
            self.max_heapify(arr, 0, length)


if __name__ == '__main__':
    arr = [1, 4, 3, 7, 8, 9, 10]
    heap = Heap()
    heap.build_max_heapify(arr)
    print arr
    arr_two = [10, 8, 9, 7, 6, 5, 4]
    heap.build_min_heapify(arr_two)
    print arr_two
    items = [(3, "Clear drains"), (4, "Feed cat"), (5, "Make tea"), (1, "Solve RC tasks"), (2, "Tax return")]
    heap.heap_short(items)
    print "\n\n"
    for x in items:
        print x

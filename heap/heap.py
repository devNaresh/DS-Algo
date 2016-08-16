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


class HeapMap(object):
    def __init__(self, data=None, heap_list=None):
        self._heap_map_list = heap_list
        self._heap_dic = data
        if data is not None and heap_list is None:
            keys = data.keys()
            self._heap_map_list = [key for key in keys]
        self._length = len(self._heap_map_list)

    def is_empty_heap(self):
        if self._heap_map_list:
            return False
        else:
            return True

    def min_heapify(self, i, length):
        if length == 0:
            return
        else:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < length and self._heap_dic[self._heap_map_list[left]] < self._heap_dic[self._heap_map_list[i]]:
                smallest = left
            if right < length and self._heap_dic[self._heap_map_list[right]] < \
                    self._heap_dic[self._heap_map_list[smallest]]:
                smallest = right
            if smallest != i:
                self._heap_map_list[i], self._heap_map_list[smallest] = self._heap_map_list[smallest], \
                                                                        self._heap_map_list[i]
                self.min_heapify(smallest, length)

    def build_min_heapify(self):
        for i in reversed(xrange(self._length / 2)):
            self.min_heapify(i, self._length)

    def max_heapify(self, i, length):
        if length == 0:
            return
        else:
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < length and self._heap_dic[self._heap_map_list[left]] > self._heap_dic[self._heap_map_list[i]]:
                largest = left
            if right < length and self._heap_dic[self._heap_map_list[right]] > \
                    self._heap_dic[self._heap_map_list[largest]]:
                largest = right
            if largest != i:
                self._heap_map_list[i], self._heap_map_list[largest] = self._heap_map_list[largest], \
                                                                       self._heap_map_list[i]
                self.min_heapify(largest, length)

    def build_max_heapify(self):
        for i in reversed(xrange(self._length / 2)):
            self.max_heapify(i, self._length)

    def heap_short(self):
        length = self._length
        self.build_max_heapify()
        for i in reversed(xrange(length)):
            self._heap_map_list[0], self._heap_map_list[i] = self._heap_map_list[i], self._heap_map_list[0]
            length -= 1
            self.max_heapify(0, length)

    def min_element(self):
        return self._heap_map_list[0]

    def pop_min_element(self):
        min_element = self._heap_map_list[0]
        last_element = self._heap_map_list.pop()
        element_value = self._heap_dic.pop(min_element, None)
        self._length -= 1
        if self._heap_map_list:
            self._heap_map_list[0] = last_element
            self.min_heapify(0, self._length)
        return min_element, element_value


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

    print "\n\n"

    items = {"3": "Clear drains", "4": "Feed cat", "5": "Ake tea", "1": "Solve RC tasks", "2": "Tax Redumtion"}
    heap_list = [key for key in items.keys()]
    hm = HeapMap(data=items, heap_list=heap_list)
    hm.heap_short()
    for x in heap_list:
        print items[x]

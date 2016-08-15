__author__ = 'naresh'

from heap import Heap


class PriorityQueue(Heap):
    def max_element(self, arr):
        return arr[0]

    def pop_max_element(self, arr):
        min_element = arr[0]
        last_element = arr.pop()
        if arr:
            arr[0] = last_element
            self.max_heapify(arr, 0, len(arr))
        else:
            min_element = last_element
        return min_element

    # check on web
    def insert_element(self, arr, value):
        length = len(arr)
        arr.append(value)
        i = length
        while i > 0 and arr[i / 2] < arr[i]:
            arr[i / 2], arr[i] = arr[i], arr[i / 2]
            i = i / 2


if __name__ == "__main__":
    arr = [8, 7, 4, 3, 1]
    pq = PriorityQueue()
    pq.insert_element(arr, 6)
    print arr
    pq.pop_max_element(arr)
    print arr

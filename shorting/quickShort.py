## WAP to implement Quick Short

def partition(arr, first, last):
    key = arr[last]
    point = first
    for i in range(first, last):
        if arr[i] <= key:
            arr[i], arr[point] = arr[point], arr[i]
            point += 1
    arr[last], arr[point] = arr[point], arr[last]
    return point


def _quick_short(first, last, arr):
    if first < last:
        splitpoint = partition(arr, first, last)
        _quick_short(first, splitpoint - 1, arr)
        _quick_short(splitpoint, last, arr)


def quick_short(arr):
    _quick_short(0, len(arr) - 1, arr)


if __name__ == "__main__":
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_short(arr)
    print arr

__author__ = '__naresh__'


def binary_search(x, arr=None, left=0, right=-1):
    if right == -1:
        right = len(arr) - 1
    if right > left:
        mid = left + (right - left) / 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return binary_search(x, arr, mid, right)
        else:
            return binary_search(x, arr, left, mid)

    else:
        return None


if __name__ == "__main__":
    arr = [0, 2, 3, 4, 10, 40, 44]

    print binary_search(10, arr)

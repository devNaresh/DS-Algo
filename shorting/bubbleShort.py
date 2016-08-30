## WAP for Bubble Short

def bubble_sort(arr):
    for i in range(1, len(arr)):
        for k in range(0, i):
            if arr[k] > arr[i]:
                arr[i], arr[k] = arr[k], arr[i]
    return arr


if __name__ == "__main__":
    arr = [7, 2, 5, 8, 1, 9, 45, 21, 545, 95]
    print bubble_sort(arr)

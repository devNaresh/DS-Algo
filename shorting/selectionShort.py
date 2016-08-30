## WAP for Selection Short

def selection_sort(arr):
    for i in range(len(arr)):
        least = i
        for k in range(i + 1, len(arr)):
            if arr[k] < arr[least]:
                least = k
        arr[i], arr[least] = arr[least], arr[i]

    return arr


if __name__ == "__main__":
    arr = [7, 2, 5, 8, 1, 9, 45, 21, 545, 95]
    print selection_sort(arr)

## WAP for Insertion Short

def Insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        k = i
        while k > 0 and arr[k - 1] > temp:
            arr[k - 1], arr[k] = arr[k], arr[k - 1]
            k = k - 1
        #arr[k] = temp
    return arr


if __name__ == "__main__":
    arr = [7, 2, 5, 8, 1, 9, 45, 21, 545, 95]
    print Insertion_sort(arr)

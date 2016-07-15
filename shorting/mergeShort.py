## WAP to implement merge short

def merge_short(arr):
    if len(arr) > 1:
        mid = len(arr) / 2
    else:
        return

    lefthalf = arr[:mid]
    righthalf = arr[mid:]
    merge_short(lefthalf)
    merge_short(righthalf)

    i = j = k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            arr[k] = lefthalf[i]
            i += 1
        else:
            arr[k] = righthalf[j]
            j += 1
        k += 1

    while i < len(lefthalf):
        arr[k] = lefthalf[i]
        i += 1
        k += 1

    while j < len(righthalf):
        arr[k] = righthalf[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_short(arr)
    print arr

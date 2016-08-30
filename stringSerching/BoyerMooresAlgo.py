__author__ = '__naresh__'

## Implementation Of BoyerMoores Algo

"""

Time Complexibility O(n + m)

https://www.youtube.com/watch?v=rDPuaNw9_Eo&list=PLTZbNwgO5ebpFlWFaorHgxHgSzcgkBLRA&index=1

Not Much efficient as it required more space based of type of characters

"""

string = "abcdefghijklmnopqrstuvwxyz "

patter_table = {}


def pre_processing(pattern):
    """
    Its create a dictionary with contains how much space a window will move

    """
    size = len(pattern)
    for x in string:
        patter_table[x] = size

    for i in range(size - 1):
        patter_table[pattern[i]] = size - 1 - i


def find_patter(orignal_string, pattern):
    pre_processing(pattern)
    size = len(pattern)
    i = size - 1
    while 0 <= i < len(orignal_string):
        if orignal_string[i] != pattern[-1]:
            i = i + patter_table[orignal_string[i]]
        else:
            found = True
            for j in reversed(range(size - 1)):
                i -= 1
                if orignal_string[i] != pattern[j]:
                    i = i + patter_table[orignal_string[i]]
                    found = False
                    break
            if found: return i
    return None


if __name__ == "__main__":
    data = "jim saw me in a barber parlour"
    pattern = "rlour"
    start = find_patter(data, pattern)
    end = start + len(pattern)
    print data[start:end]

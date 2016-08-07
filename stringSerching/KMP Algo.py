__author__ = '__naresh__'

# Implementation of KMP search algo

"""

Time Complexibility O(m+n)

https://www.youtube.com/watch?v=GTJr8OvyEVQ

"""


def pattern_preprocessing(pattern):
    """
    Things to Remember

    1) Increment value of 'i' by one once temp[i] is filled
    2) If character not match then value of 'j' will be value in temp[j-1]

    """
    temp = [0] * len(pattern)
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            temp[i] = j + 1
            j += 1
            i += 1
        else:
            if j is 0:
                temp[i] = 0
                i += 1
            else:
                j = temp[j - 1]

    return temp


def kmp_search(orignal_string, pattern):
    temp = pattern_preprocessing(pattern)
    i = j = 0

    while True:
        if orignal_string[i] != pattern[j] and j == 0:
            i += 1
        elif orignal_string[i] != pattern[j] and j != 0:
            j = temp[j - 1]
        else:
            i += 1
            j += 1
            if j == len(pattern):
                return i
    return None


if __name__ == "__main__":
    # data = "ABABDABACDABABCABAB"
    # pattern = "ABABCABAB"
    data = "jim saw me in a barber parlour"
    pattern = "barber"
    end = kmp_search(data, pattern)
    start = end - len(pattern)
    print data[start:end]

__author__ = "__naresh__"

# Given two strings str1 and str2, find the minimum number of edits (edit one character to another, delete char from str1
# or delete char from str2) to change str1 to str2.

"""
Time Complexibility O(row * col)
Space Complexibility O(row * col)

******* Formula *******

if str1[i - 1] == str2[j - 1]:
    T[i][j] = T[i - 1][j - 1]
else:
    T[i][j] = 1 + min(T[i - 1][j], T[i - 1][j - 1], T[i][j - 1])

"""


def minimum_edits(str1, str2):
    """ DP Soution """

    row = len(str1) + 1
    col = len(str2) + 1
    T = [[0] * col for _ in range(row)]
    T[0] = [i for i in range(col)]
    for i in range(row):
        T[i][0] = i

    for i in range(1, row):
        for j in range(1, col):
            if str1[i - 1] == str2[j - 1]:
                T[i][j] = T[i - 1][j - 1]
            else:
                T[i][j] = 1 + min(T[i - 1][j], T[i - 1][j - 1], T[i][j - 1])

    for i in T:
        print i

    print "-" * 20
    i = row - 1
    j = col - 1

    while i > 0 and j > 0:
        if T[i][j] == 1 + T[i - 1][j - 1] and str1[i - 1] != str2[j - 1]:
            print "Replace {0} with {1} at {2}".format(str2[j - 1], str1[i - 1], j - 1)
            i -= 1
            j -= 1

        elif T[i][j] == T[i - 1][j - 1] and str1[i - 1] == str2[j - 1]:
            i -= 1
            j -= 1

        elif T[i][j] == 1 + T[i][j - 1]:
            j -= 1
            print "Delete {0} at {1}".format(str2[j], j)
        else:
            i -= 1
            print "Add {0} at {1}".format(str1[i], i)


def minimum_edits_recusive(str1, str2):
    """ Recursive Soution """

    i = len(str1)
    j = len(str2)

    if i == 0:
        return j
    if j == 0:
        return i

    return min(minimum_edits_recusive(str1[:i - 1], str2) + 1,
               minimum_edits_recusive(str1, str2[:j - 1]) + 1,
               minimum_edits_recusive(str1[:i - 1], str2[:j - 1]) + (1 if str1[i - 1] != str2[j - 1] else 0))


if __name__ == '__main__':
    str_1 = "azced"
    str_2 = "abcdef"
    print minimum_edits_recusive(str_1, str_2)

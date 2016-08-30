__author__ = '__naresh__'


# WAP to find longest common sub-sequence between two strings


"""
Time Complexibility O(n^2)
Space Complexibility O(n^2)

******* Formula *******

if string[i] == string[j]:
    T[i][j] = 1 + T[i-1][j-1]
else:
    T[i][j] = max(T[i-1][j], T[i][j-1])

"""


def find_lcs(str1, str2):
    col = len(str1)
    row = len(str2)

    table = [[0] * (col + 1) for _ in range(row + 1)]

    for i, x in enumerate(str2, start=1):
        for j, y in enumerate(str1, start=1):
            if x == y:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])

    for x in table:
        print x

    x, y = row, col

    result = ""

    while x > 0 and y > 0:
        if str2[x - 1] == str1[y - 1]:
            result += str2[x - 1]
            x -= 1
            y -= 1
        elif table[x][y] == table[x-1][y]:
            x -= 1
        elif table[x][y] == table[x][y-1]:
            y -= 1
    print result[::-1]


if __name__ == '__main__':
    str1 = "ABCBDAB"
    str2 = "BDCABA"
    find_lcs(str1, str2)

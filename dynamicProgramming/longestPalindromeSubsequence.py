__author__ = '__naresh__'

"""
Time Complexibility O(n^2)
Space Complexibility O(n^2)

******* Formula *******

if string[i] == string[j]:
    T[i][j] = 2 + T[i+1][j-1]
else:
    T[i][j] = max(T[i+1][j], T[i][j-1])

"""

def longest_palindrome_subsequence(string):
    str_length = len(string)
    table = [[0] * str_length for _ in range(str_length)]

    for i in range(str_length):
        table[i][i] = 1

    for length in range(2, str_length + 1):
        for row in range(0, str_length - length + 1):
            col = row + length - 1

            if string[row] == string[col]:
                table[row][col] = 2 + table[row + 1][col - 1]
            else:
                table[row][col] = max(table[row + 1][col], table[row][col - 1])

    for x in table:
        print x

    x = 0
    y = str_length
    length = table[x][y - 1]
    i = 0
    palindrome = [0] * length
    while x <= y:
        if string[x] == string[y - 1]:
            palindrome[i] = string[x]
            palindrome[length - i - 1] = string[y - 1]
            x += 1
            y -= 1
            i += 1
        elif table[x + 1][y] == table[x][y]:
            x += 1
        else:
            y -= 1

    print palindrome


if __name__ == "__main__":
    string = "agbdba"
    longest_palindrome_subsequence(string)

"""
Time Complexibility O(str1_len * str2_len)
Space Complexibility O(str1_len * str2_len)

******* Formula *******

if string[i-1] == string[j-1]:
    T[i][j] = 1 + T[i - 1][j - 1]j-1]

"""


def longest_common_subsequence(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    row = length1 + 1
    col = length2 + 1
    T = [[0] * (col) for _ in range(row)]

    for i in range(1, row):
        for j in range(1, col):
            if str1[i - 1] == str2[j - 1]:
                T[i][j] = 1 + T[i - 1][j - 1]

    print max(max(c) for c in T)

if __name__ == "__main__":
    str1 = "tutorialhorizon"
    str2 = "dynamictutorialProgramming"

    longest_common_subsequence(str1, str2)

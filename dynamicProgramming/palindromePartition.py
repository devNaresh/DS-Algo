# Prtition a word so that we get minimum palindromes
"""
Time Complexibility O(n^2)
Space Complexibility O(n^2)

*** Refereance ***

https://www.youtube.com/watch?v=WPr1jDh3bUQ
http://www.geeksforgeeks.org/dynamic-programming-set-17-palindrome-partitioning/

"""

def palindrom_partition(pal):
    length = len(pal)
    partition_arr = [0] * length
    pal_table = [[0] * length for _ in range(length)]
    for i in range(length):
        pal_table[i][i] = 1
    for L in range(2, length):
        for i in range(length - L):
            j = i + L
            if pal[i] == pal[j]:
                pal_table[i][j] = pal_table[i + 1][j - 1]

    for x in pal_table:
        print x

    for L in range(length):
        if pal_table[0][L] is 1:
            partition_arr[L] = 0
        else:
            partition_arr[L] = length
            for i in range(L):
                if pal_table[i + 1][L] is 1 and partition_arr[L] > \
                        partition_arr[i] + 1:
                    partition_arr[L] = partition_arr[i] + 1
    print "-" * 50
    print partition_arr

if __name__ == '__main__':
    string = "ababbbabbababa"
    string2 = "banana"
    palindrom_partition(string2)

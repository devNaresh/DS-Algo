__author__ = '__naresh__'

# WAP to find minimum number of coins required to make N

"""
Time Complexibility O(coins * total)
Space Complexibility O(coins * total)

******* Formula *******

if coins[i] > j:
    T[i][j] = T[i - 1][j]
else:
    T[i][j] = T[i][j - coins[i]] + T[i - 1][j]

"""


def min_coins(coins, total):
    cols = total + 1
    rows = len(coins)
    T = [[1] * cols for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            if coins[i] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i][j - coins[i]] + T[i - 1][j]
    for x in T:
        print x


if __name__ == '__main__':
    min_coins([1, 2, 3], 5)

__author__ = '__naresh__'

# WAP to find minimum number of coins required to make N

"""
Time Complexibility O(coins * total)
Space Complexibility O(coins * total)

******* Formula *******

if coins[i] > j:
    T[i][j] = T[i - 1][j]
else:
    T[i][j] = min(T[i][j - coins[i]] + 1, T[i - 1][j])

"""

INF = 99999999


def min_coins(coins, total):
    cols = total + 1
    rows = len(coins)
    T = [[0] + [INF] * total for _ in range(rows)]

    for i in range(rows):
        for j in range(1, cols):
            if coins[i] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = min(T[i][j - coins[i]] + 1, T[i - 1][j])
    for x in T:
        print x
    print "-" * 12
    i = rows - 1
    j = total
    while i >= 0 and j >= 0:
        if T[i][j] == 1 + T[i][j - coins[i]]:
            print coins[i],
            j -= coins[i]
        else:
            i -= 1


if __name__ == '__main__':
    min_coins([1, 5, 6, 8], 11)

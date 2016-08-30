__author__ = '__naresh__'

# WAP to find maximum path avaiable to reach particuar point in matrix you can only move right or down

"""
Time Complexibility O(n^2)
Space Complexibility O(n^2)

******* Formula *******

T[i][j] = T[i-1][j] + T[i][j-1])

"""


def matrix_path(matrix):
    """ DP Solution """
    matrix_size = len(matrix)
    path_matrix = [[1] * matrix_size for _ in range(matrix_size)]
    for i in range(1, matrix_size):
        for j in range(1, matrix_size):
            path_matrix[i][j] = path_matrix[i - 1][j] + path_matrix[i][j - 1]

    for x in path_matrix:
        print x


def _matrix_path_recursive(row, col):
    """ Recursive Solution """
    if row is 1 or col is 1:
        return 1
    return _matrix_path_recursive(row - 1, col) + _matrix_path_recursive(row, col - 1)


def matrix_path_recursive(matrix):
    row = len(matrix)
    return _matrix_path_recursive(row, row)


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    print matrix_path_recursive(matrix)

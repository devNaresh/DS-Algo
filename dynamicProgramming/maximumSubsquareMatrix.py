__author__ = "__naresh__"


# WAP to find maximum sub-squares in a matrix filled with O,X with edges X

def create_matrix_table(matrix):
    matrix_length = len(matrix)
    new_matrix = [[(0, 0)] * matrix_length for x in range(matrix_length)]
    for i in range(matrix_length):
        for j in range(matrix_length):
            if matrix[i][j] == "X":
                if i is 0 and j is not 0:
                    new_matrix[i][j] = 1, new_matrix[i][j - 1][1] + 1
                elif i is not 0 and j is 0:
                    new_matrix[i][j] = new_matrix[i - 1][j][0] + 1, 1
                else:
                    new_matrix[i][j] = new_matrix[i - 1][j][0] + 1, new_matrix[i][j - 1][1] + 1
    return new_matrix


def find_maximum_subsquare(matrix):
    matrix_len = len(matrix)
    max_sub_square = 0
    matrix_table = create_matrix_table(matrix)
    for i in matrix_table:
        print i

    for i in reversed(range(matrix_len)):
        for j in reversed(range(matrix_len)):
            minimum = min(matrix_table[i][j])
            while minimum > 0 and minimum > max_sub_square:
                if matrix_table[i - minimum + 1][j][1] >= minimum and matrix_table[i][j - minimum+1][0] >= minimum:
                    max_sub_square = minimum
                minimum -= 1

    return max_sub_square


if __name__ == "__main__":
    matrix = [['O', 'O', 'O', 'O', 'X'],
              ['X', 'O', 'X', 'X', 'X'],
              ['X', 'O', 'X', 'O', 'X'],
              ['X', 'X', 'X', 'X', 'X'],
              ['O', 'O', 'X', 'X', 'X']]
    print find_maximum_subsquare(matrix)

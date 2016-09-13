# WAP to query sum in 2D array in constant time

"""
Time Complexibility O(1)
Space Complexibility O(len(arr))

"""


from collections import namedtuple

Maxtrix = namedtuple("Matrix", "rows cols")


class Query2DArray:

    def __init__(self, arr):
        self.row = len(arr) + 1
        self.col = len(arr[0]) + 1
        self.T = [[0] * self.col for _ in range(self.row)]
        self.create_matrix(arr)

    def create_matrix(self, arr):
        for i in range(1, self.row):
            for j in range(1, self.col):
                self.T[i][j] = self.T[i][j - 1] + self.T[i - 1][j] - \
                    self.T[i - 1][j - 1] + arr[i - 1][j - 1]

    def findSum(self, start, end):
        start = Maxtrix(start.rows + 1, start.cols + 1)
        end = Maxtrix(end.rows + 1, end.cols + 1)
        return self.T[end.rows][end.cols] - self.T[start.rows - 1][end.cols] \
            - self.T[end.rows][start.cols - 1] + \
            self.T[start.rows - 1][start.cols - 1]

if __name__ == "__main__":
    start = Maxtrix(3, 2)
    end = Maxtrix(4, 4)
    arr = [[3, 0, 1, 4, 2],
           [5, 6, 3, 2, 1],
           [1, 2, 0, 1, 5],
           [4, 1, 0, 1, 7],
           [1, 0, 3, 0, 5]]
    obj = Query2DArray(arr)
    print "Sum is =", obj.findSum(start, end)

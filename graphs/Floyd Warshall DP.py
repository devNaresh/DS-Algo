__author__ = '__naresh__'

## Implementation of Floyd WarShall Algorithm

"""

Time Complexibility O(V3)
Space Compexibility O(V2)

https://www.youtube.com/watch?v=LwJdNfdLF9s&list=PLrmLmBdmIlpu2f2g8ltqaaCZiq6GJvl1j&index=7

"""

INF = 999999999


class FloydWarshall:
    def __init__(self, graph):
        self.__distance_dic = {}
        self.__path_dic = {}
        nodes = graph.keys()
        for i in nodes:
            self.__distance_dic[i] = {}
            self.__path_dic[i] = {}
            for j in nodes:
                self.__distance_dic[i][j] = graph[i][j]
                if self.__distance_dic[i][j] is not INF and i != j:
                    self.__path_dic[i][j] = i
                else:
                    self.__path_dic[i][j] = -1

        for k in nodes:
            for i in nodes:
                for j in nodes:
                    if self.__distance_dic[i][j] > self.__distance_dic[i][k] + self.__distance_dic[k][j]:
                        self.__distance_dic[i][j] = self.__distance_dic[i][k] + self.__distance_dic[k][j]
                        self.__path_dic[i][j] = self.__path_dic[k][j]

    @staticmethod
    def print_solution(data):
        nodes = data.keys()
        print "   ",
        for i in nodes:
            print "   {0:3}".format(i),
        print "\n",

        for i in nodes:
            print "\n",
            print i,
            for j in nodes:
                if data[i][j] is INF:
                    print "   {0}".format("INF"),
                else:
                    print "   {0:3}".format(data[i][j]),

    def print_distance(self):
        self.print_solution(self.__distance_dic)

    def print_path(self):
        self.print_solution(self.__path_dic)

    def get_distance(self, i, j):
        return self.__distance_dic[i][j]

    def get_path(self, i, j):
        path = []
        path.append(j)
        while self.__path_dic[i][j] != i:
            path.append(self.__path_dic[i][j])
            j = self.__path_dic[i][j]
        path.append(i)
        return path[::-1]


if __name__ == '__main__':
    graph = {'A': {'A': 0, 'B': 6, 'C': INF, 'D': 6, 'E': 7},
             'B': {'A': INF, 'B': 0, 'C': 5, 'D': INF, 'E': INF},
             'C': {'A': INF, 'B': INF, 'C': 0, 'D': 9, 'E': 3},
             'D': {'A': INF, 'B': INF, 'C': 9, 'D': 0, 'E': 7},
             'E': {'A': INF, 'B': 4, 'C': INF, 'D': INF, 'E': 0}
             }
    fm = FloydWarshall(graph)
    print fm.get_path("B", "D")

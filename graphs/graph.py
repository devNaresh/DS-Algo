__author__ = 'naresh'


class Graph(object):
    def __init__(self, graph_dic=None):
        if graph_dic is not None:
            self.__graph_dic = graph_dic
        else:
            self.__graph_dic = {}

    def get_vertex(self):
        return self.__graph_dic.keys()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dic.keys():
            self.__graph_dic[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.__graph_dic.keys():
            self.__graph_dic[vertex1].append(vertex2)
        else:
            self.__graph_dic[vertex1] = vertex2

    def get_edges(self):
        edges = []
        for key, value in self.__graph_dic.items():
            for x in value:
                edges.append((key, x))
        return edges

    def dfs(self, start):
        visited, stack = [], [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                for x in self.__graph_dic[vertex]:
                    if x not in visited:
                        stack.append(x)
        return visited

    def dfs_recursive(self, start, visited=None):
        if visited is None:
            visited = []
        if start not in visited:
            visited.append(start)
        for x in self.__graph_dic[start]:
            if x not in visited:
                self.dfs_recursive(x, visited)
        return visited

    def dfs_path(self, start, goal):
        path = []

if __name__ == "__main__":
    g = {"a": ["b", "c"],
         "b": ["a", "d", "e"],
         "c": ["a", "f"],
         "d": ["b"],
         "e": ["b", "f"],
         "f": ["c", "e"]
         }

    graph = Graph(g)
    print graph.dfs_recursive("c")

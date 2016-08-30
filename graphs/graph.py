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
            self.__graph_dic[vertex1] = [vertex2]

    def depth_first_serarch(self, start):
        visited = []
        stack = []
        stack.append(start)
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                stack.extend([node for node in self.__graph_dic[vertex] if node not in visited])
        return visited

    def dfs_recursive(self, node, visited=None):
        if visited is None:
            visited = []
        if node in visited:
            return
        else:
            visited.append(node)
            for each in (x for x in self.__graph_dic[node] if x not in visited):
                self.dfs_recursive(each, visited)
        return visited

    def dfs_path(self, start, goal, path=None):
        if path is None:
            path = [start]
        if start == goal:
            yield path
        data = [x for x in self.__graph_dic[start] if x not in path]
        for vertex in data:
            # yield from self.dfs_path(vertex, goal, path + [vertex])
            for each_path in self.dfs_path(vertex, goal, path + [vertex]):
                yield each_path
        return

    def breath_first_search(self, start):
        visited, queue = [], [start]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
            for vertex in self.__graph_dic[node]:
                if vertex not in visited:
                    queue.append(vertex)
                    visited.append(vertex)
        return visited

    def bfs_path(self, start, end):
        queue = [(start, [start])]
        while queue:
            node, path = queue.pop(0)
            if node == end:
                yield path
            for vertex in self.__graph_dic[node]:
                if vertex not in path:
                    queue.append((vertex, path + [vertex]))


class WeightedGraph(object):
    def __init__(self, graph_dic=None, directed=True):
        self.directed = directed
        if graph_dic is not None:
            self.__graph_dic = graph_dic
        else:
            self.__graph_dic = {}

    def get_vertex(self):
        return self.__graph_dic.keys()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dic.keys():
            self.__graph_dic[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.__graph_dic[vertex1][vertex2] = weight
        if not self.directed:
            self.__graph_dic[vertex2][vertex1] = weight

    def get_edges(self):
        edges = {}
        for key, value in self.__graph_dic.items():
            for k, v in value.items():
                edge = (key, k)
                if self.directed or (edge not in edges and edge[::-1] not in edges):
                    edges[edge] = v
        return edges

    def get_graph(self):
        return self.__graph_dic

    if __name__ == "__main__":
        graph = {"a": ["b", "c"],
                 "b": ["a", "d", "e"],
                 "c": ["a", "f"],
                 "d": ["b"],
                 "e": ["b", "f"],
                 "f": ["c", "e"]
                 }

        # graph = {'A': ['B', 'C', 'D'],
        #          'B': ['A', 'E', 'F'],
        #          'C': ['A', 'F'],
        #          'D': ['A'],
        #          'E': ['B'],
        #          'F': ['B', 'C']}

        graph = Graph(graph)
        # print(graph.depth_first_serarch("A"))
        print(list(graph.bfs_path("a", "f")))



        # ['a', 'b', 'd', 'e', 'f', 'c']
        # ['a', 'c', 'f', 'e', 'b', 'd']
        # [['a', 'b', 'e', 'f'], ['a', 'c', 'f']]

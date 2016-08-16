__author__ = '__naresh__'

"""

Time Complexibility O(E log(V))
Space Compexibility O(E+V)

https://www.youtube.com/watch?v=lAXZGERcDf4&index=2&list=PLrmLmBdmIlpu2f2g8ltqaaCZiq6GJvl1j

"""
from heap.heap import HeapMap
from graph import WeightedGraph

INF = 999999999


def dijkastra_algo(graph, source_vertex):
    distance = {}
    path = {}
    nodes = graph.keys()
    min_heap_dic = {key: INF for key in nodes}
    min_heap_dic[source_vertex] = 0
    path[source_vertex] = 0
    hm = HeapMap(data=min_heap_dic)
    while not hm.is_empty_heap():
        hm.build_min_heapify()
        vertex, value = hm.pop_min_element()
        distance[vertex] = value
        for edge in graph[vertex]:
            if edge in min_heap_dic and graph[vertex][edge] + distance.get(vertex, 0) < min_heap_dic[edge]:
                min_heap_dic[edge] = graph[vertex][edge] + distance.get(vertex, 0)
                path[edge] = vertex

    return path, distance


if __name__ == "__main__":
    graph = WeightedGraph(directed=False)
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 8, 2)
    graph.add_edge(2, 5, 4)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)

    path, distance = dijkastra_algo(graph.get_graph(), 0)

    for key, value in distance.items():
        print "{0} to {1} distance = {2}".format(0, key, value)

    print "*" * 50

    for vertex in graph.get_vertex():
        x = vertex
        path_list = []
        while x != 0:
            path_list.append(x)
            x = path[x]
        path_list.append(0)
        print "Shortest Path from 0 to {0} is {1}".format(vertex, path_list[::-1])

__author__ = '__naresh__'

# Find Minimum Spam tree using Prim's Algorithm

"""

Time Complexibility O(E log(V))
Space Compexibility O(E+V)

https://www.youtube.com/watch?v=oP2-8ysT3QQ

"""

from heap.heap import HeapMap
from graph import WeightedGraph

INF = 99999999


def prims_algo(graph):
    result = []
    nodes = graph.keys()
    min_heap_dic = {key: INF for key in nodes}
    edge_dic = {}
    min_heap_dic['A'] = 0
    hm = HeapMap(data=min_heap_dic)
    while not hm.is_empty_heap():
        hm.build_min_heapify()
        node, _ = hm.pop_min_element()
        if node in edge_dic:
            result.append(edge_dic[node])
        for vertex in graph[node]:
            if vertex in min_heap_dic and graph[node][vertex] < min_heap_dic[vertex]:
                min_heap_dic[vertex] = graph[node][vertex]
                edge_dic[vertex] = "{0}{1}".format(node, vertex)

    return result


if __name__ == "__main__":
    graph = WeightedGraph(directed=False)
    # graph = {'A': {'A': INF, 'B': 3, 'C': INF, 'D': 1, 'E': INF, 'F': INF},
    #          'B': {'A': 3, 'B': INF, 'C': 1, 'D': 3, 'E': INF, 'F': INF},
    #          'C': {'A': INF, 'B': 1, 'C': INF, 'D': 1, 'E': 5, 'F': 4},
    #          'D': {'A': 1, 'B': 3, 'C': 1, 'D': INF, 'E': 6, 'F': INF},
    #          'E': {'A': INF, 'B': INF, 'C': 5, 'D': 6, 'E': INF, 'F': INF},
    #          'F': {'A': INF, 'B': INF, 'C': 4, 'D': INF, 'E': 2, 'F': INF}
    #          }
    graph.add_edge('A', 'B', 3)
    graph.add_edge('A', 'D', 1)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 3)
    graph.add_edge('C', 'D', 1)
    graph.add_edge('C', 'E', 5)
    graph.add_edge('C', 'F', 4)
    graph.add_edge('D', 'E', 6)
    graph.add_edge('F', 'E', 2)
    result = prims_algo(graph.get_graph())
    print result


# ['AD', 'DC', 'CB', 'CF', 'FE']
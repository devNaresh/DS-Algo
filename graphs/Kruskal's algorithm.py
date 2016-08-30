__author__ = '__naresh__'

"""

Time Complexibility O(E log(E))
Space Compexibility O(E+V)

https://www.youtube.com/watch?v=fAuF0EuZVCk

"""

from graph import WeightedGraph
from disjointSets.disjointSets import DisjointSet


def kruskal_algo(graph):
    ds = DisjointSet()
    result = []
    edges = graph.get_edges()
    map(ds.make_set, graph.get_vertex())
    for edge, _ in (x for x in sorted(edges.items(), key=lambda (key, value): value)):
        node1 = ds.find_set(edge[0])
        node2 = ds.find_set(edge[1])
        if node1 == node2:
            continue
        else:
            result.append("{0}{1}".format(*edge))
            ds.union(*edge)
    return result


if __name__ == "__main__":
    graph = WeightedGraph(directed=False)
    graph.add_edge('A', 'B', 3)
    graph.add_edge('A', 'D', 1)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 3)
    graph.add_edge('C', 'D', 1)
    graph.add_edge('C', 'E', 5)
    graph.add_edge('C', 'F', 4)
    graph.add_edge('D', 'E', 6)
    graph.add_edge('F', 'E', 2)
    print kruskal_algo(graph)

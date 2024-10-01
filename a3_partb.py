#Student name: Samarth Patel

from a2d import Graph
from a3_parta import MinHeap

def minimum_spanning_tree(graph):
    mst = []
    visited = set()
    heap = MinHeap([(0, 0, None)]) # (weight, vertex, previous vertex)
    while not heap.is_empty():
        weight, curr, prev = heap.extract_min()
        if curr in visited:
            continue
        visited.add(curr)
        if prev is not None:
            mst.append((prev, curr))
        for neighbor, weight in graph.adjacency_list[curr]:
            if neighbor not in visited:
                heap.insert((weight, neighbor, curr))
    return mst

# look at this for import later
# https://www.youtube.com/watch?v=X1cwEKfRZJE

# try:
#     import os
#     import sys
#     from ..graph.graph import graph
# except Exception as e:
    # print(f"Something went wrong: {e}")

from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # if the input does not have parents, return a -1
    # base case?
    # if starting_node has no parent, it should return -1
    # ESSENTIALLY: We want to reverse our search up the "tree" 
    graph = Graph()

    # Simpler way from Kerri Ann Bates
    # added = []
    # for pair in ancestors:
    #     for item in pair:
    #         if item not in added:
    #             graph.add_vertex(item)
    #             added.append(item)

    #     graph.add_edge(pair[1], pair[0])

    for i in ancestors:
        if i[0] in graph.vertices and i[1] not in graph.vertices:
            graph.add_vertex(i[1])
        elif i[1] in graph.vertices and i[0] not in graph.vertices:
            graph.add_vertex(i[0])
        elif i[0] in graph.vertices and i[1] in graph.vertices:
            pass
        else:
            graph.add_vertex(i[0])
            graph.add_vertex(i[1])

    for i in ancestors: 
        # We want to reverse these edges since 11, 10, 4 and 2 will not have neighbors
        graph.add_edge(i[1], i[0])
    
    # visited = graph.dft(starting_node) # goes through the depth
    revisited = graph.bft(starting_node) # goes through the breadth 
    last = revisited[-1]
    if last == starting_node:
        return -1
    else:
        return last


# junk code 
    
    


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 10)


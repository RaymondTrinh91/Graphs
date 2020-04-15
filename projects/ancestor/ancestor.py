from projects.graph.graph import Graph

# def helper(ancestors):
#     gg = Graph()

#     for pair in ancestors:
#         parent = pair[0]
#         child = pair[1]
        
#         if parent not in gg.vertices:
#             gg.add_vertex(parent)
#         if child not in gg.vertices:
#             gg.add_vertex(child)
#         gg.add_edge(child, parent)
    
#     return gg


def earliest_ancestor(ancestors, starting_node):
    graph = graph.Graph()

    # added = []

    for pair in ancestors:
        for item in pair:
            if item not in graph.vertices:
                graph.add_vertex(item)
            # if item not in added:
            #     graph.add_vertex(item)
            #     added.append(item)

    for i in ancestors:
        graph.add_edge(i[1], i[0])

    revisited = graph.bft(starting_node)
    last = revisited[-1]

    if last == starting_node:
        return -1
    else:
        return last
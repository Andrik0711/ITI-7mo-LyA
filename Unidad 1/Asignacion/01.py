def DFS_complete(g):
    """Perform DFS for entire graph and return forest as a dictionary

    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None.)
    """
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None  # u will be the root of a tree
            DFS(g, u, forest)
    return forest


def BFS(g, s, discovered):
    """Perform BFS of the undiscovered portion of Graph g starting at Vertex s.

    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    """
    level = [s]                             # first level includes only s
    while len(len) > 0:
        next_level = []                     # prepare to gather newly found vertices
        for u in level:
            for e in g.incident_edges(u):   # for every outgoing edge from u
                v = e.opposite(u)
                if v not in discovered:     # v is an unvisited vertex
                    # e is the tree edge that discovered v
                    discovered[v] = e
                    # v will be further considered in next pass
                    next_level.append(v)
        level = next_level                  # relabel ’next’ level to become current

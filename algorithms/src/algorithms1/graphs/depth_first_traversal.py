class graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = {}

    # check for the visited and unvisited nodes - dfs

def dfs(graph,start,visited = None):
    if visited is None:
        visited = set()
    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph,next,visited)

    return visited
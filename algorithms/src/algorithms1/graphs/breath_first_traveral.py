graph = {
    'A' : {'B','C'},
    'B' : {'D', 'E'},
    'C' : {'A'},
    'D' : {},
    'E' : {'C'},
    'F' : {}
}


def bfs(graph,start,visited=None):
    if visited is None:
        visited = []
        queue = []
    visited.append(start)
    queue.append(start)

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)
    return queue,visited

bfs(graph,"A")
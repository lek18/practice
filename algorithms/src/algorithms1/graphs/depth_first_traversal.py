class graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addVertex(self,node1,node2):
        if node1 not in self.gdict:
            self.gdict[node1] = {node2}
        else:
            self.gdict[node1].add(node2)

    # check for the visited and unvisited nodes - dfs

# this uses a se




def dfs(graph,start,visited=None):
    if visited is None:
        visited=[]
    if start not in visited:
        visited.append(start)
        print(start)
        # track.append(start)
        # visit every node adjacent to start
        for neighbour in graph[start]:
            dfs(graph,neighbour,visited)
    return visited


graph = {
    'A' : {'B','C'},
    'B' : {'D', 'E'},
    'C' : {'F','A'},
    'D' : {},
    'E' : {'F'},
    'F' : {'C'}
}
dfs(graph,"E")








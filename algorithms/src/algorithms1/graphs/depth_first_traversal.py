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

def dfs(graph,start,visited = None):
    # steps = []
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    if start in graph:
        for next in graph[start] - visited:
            dfs(graph,next,visited)

    return visited


## disconnected graph
disc_vertices = [[0,2],[2,1],[1,0],[1,2],[0,3]]

#create graph
myDisconnectedGraph = graph()
for node1,node2 in disc_vertices:
    myDisconnectedGraph.addVertex(node1,node2)


myDisconnectedGraph.gdict

myDisconnectedGraph.addVertex(node1,node2)

dfs(start=0,graph=myDisconnectedGraph.gdict)

### a not disconnected graph

gdict = { 0 : set([1,2)}

dfs(gdict,0)
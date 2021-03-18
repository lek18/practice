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
    # if start in graph:
    for next in graph[start] - visited:
        dfs(graph,next,visited)
    return visited

# breath first search
# this uses a queue
import collections
def bfs2(graph, start):
    seen, queue = set([start]), [start]
    while queue:
        vertex = queue.pop(0)
        print(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)



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

gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }

# dfs(gdict,0)
bfs(gdict,"b") == bfs2(gdict,"b")

def bfs(graph, startnode):
# Track the visited and unvisited nodes using queue
        seen, queue = set([startnode]), collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            print(vertex)
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)


bfs2(gdict,"a")
dfs(gdict,"a")
class Graph:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # get the keys of a dictionary
    def getVertices(self):

       return list(self.gdict.keys())

    # get all distinct edges from a graph
    def getAllDistinctEdges(self):
        all_edges = []

        for node in self.gdict.keys():
            for nxtnode in self.gdict[node]:
                if sorted([nxtnode,node]) not in all_edges:
                    all_edges.append(sorted([nxtnode,node]))
        return all_edges

    # get all edges
    def getAlledges(self):
        all_edges = []

        for node in self.gdict.keys():
            for nxtnode in self.gdict[node]:
                all_edges.append(sorted([node,nxtnode]))
        return all_edges

    # add a vertex
    def addVertex(self,vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []

# example
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = Graph(graph_elements)

g.getAlledges()
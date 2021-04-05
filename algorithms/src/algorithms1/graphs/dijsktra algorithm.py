def dijstra_shortespath(graph, start, target):

    # define costs and parents dictionaries to hold track of our progress
    costs = {}
    parents = {}
    for keys in graph:
        costs[keys] = 2e31 if keys !=start else 0 #very large number
    # print(costs)
    current_node = start
    while current_node!=target:
        # record the costs for stepping into its neighbour nodes
        # update it ie if its smaller than what we currently have
        for neighbour in graph[current_node]:
            if graph[current_node][neighbour] + costs[current_node] < costs[neighbour]: #
                costs[neighbour] = graph[current_node][neighbour]
                # save its link ie its parent of the current node
                parents[neighbour] = current_node
            # delete the link of current to neighbour - if it exists
            if graph[neighbour].get(current_node):
                del graph[neighbour][current_node]
        # print(costs)
        del costs[current_node] # delete it bc now ur focused on the next node!
        # remove the costs of the current node and repeat above with the next node that has minimum costs
        current_node = min(costs,key=costs.get)

    return parents

graph = {'A': {'C': 5, 'D': 1, 'E': 2}, 'B': {'H': 1, 'G': 3}, 'C': {'I': 2, 'D': 3},
         'D': {'C': 3, 'A': 1, 'H': 2}, 'E': {'A': 2, 'F': 3},
         'F': {'E': 3, 'G': 1}, 'G': {'F': 1, 'B': 3, 'H': 2}, 'H': {'I': 2, 'D': 2, 'B': 1, 'G': 2},
         'I': {'C': 2, 'H': 2}}

traces = dijstra_shortespath(graph=graph,start="A",target="B")

def shortesPath(traces,start,target):
    output = []

    current = target
    # output.append(current)
    # need to the search backwards.
    while current!=start:
        output.append(current)
        current = traces[current]
    output.append(start)
    return output[::-1]

shortesPath(traces,"A","B")
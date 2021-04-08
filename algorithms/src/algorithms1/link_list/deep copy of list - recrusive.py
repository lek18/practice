class Node(object):
    def __init__(self,x,next=None,random=None):
        self.val = x
        self.next = next
        self.random = random


class Solution(object):
    def __init__(self):
        # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
        self.visited = {}

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        # base case
        if head is None:
            return head
        # check if node is in visited
        if head in self.visited:
            return self.visited[head]

        # create new node
        newnode = Node(head.val,None,None)

        # add it to hashmapu
        self.visited[head] = newnode

        newnode.next = self.copyRandomList(head.next)
        newnode.random = self.copyRandomList(head.random)

        return newnode
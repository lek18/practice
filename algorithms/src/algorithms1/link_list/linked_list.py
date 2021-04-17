# Node class
class Node:
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize
    # next as null


# Linked List class
class LinkedList:

    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    def recursiveHelper(self,node):
        if node:
            print(node.data)
            self.recursiveHelper(node.next)

    def printList(self,method):
        if method == "iterative":
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
        elif method =="recrusive":
            current = self.head
            self.recursiveHelper(node = current)

        else:
            return "Method not possible"


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n1.next = n2
n2.next = n3
n3.next = n4

llist = LinkedList()
llist.head

# attached 1 as the head
llist.head = n1
llist.printList(method="iterative")
llist.printList(method="recrusive")


# # traversing a linked list
# class Node:
#     def __init__(self, dataval=None):
#         self.dataval = dataval
#         self.nextval = None

# class SLinkedList:
#     def __init__(self):
#         self.headval = None

#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print (printval.dataval)
#             printval = printval.nextval

# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
# e4 = Node("thue")
# # Link first Node to second node
# list.headval.nextval = e2

# #list.headval.nextval.nextval = e3
# #list.headval.nextval.nextval=e3
# # Link second Node to third node. how are these two equivalent, e2 is separate from list.headval.nextval
# e2.nextval = e3
# e3.nextval = e4

# list.listprint()



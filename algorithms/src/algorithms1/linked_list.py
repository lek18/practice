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

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

llist = LinkedList()
llist.head

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
# attached 1 as the head
llist.head = n1
llist.head.next = n2
llist.head.next.next = n3
llist.head.next.next.next = n4

llist.head.data
llist.head.next.data
llist.head.next.next.data
llist.head.next.next.next.data

a = range(0,100)

# traversing a linked list
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("thue")
# Link first Node to second node
list.headval.nextval = e2

#list.headval.nextval.nextval = e3
#list.headval.nextval.nextval=e3
# Link second Node to third node. how are these two equivalent, e2 is separate from list.headval.nextval
e2.nextval = e3
e3.nextval = e4

list.listprint()

class test1:
    def __init__(self,name = None):
        self.name = name

a =test1()

class test2:
    def __init__(self,grade= None):
        self.grade= grade


a = test1()
b = test2()

a.name=b

a.name.grade

b.grade=20

a.name.grade
b.grade
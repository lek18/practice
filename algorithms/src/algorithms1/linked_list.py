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


def test_link_list():
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    ''' 
    Three nodes have been created. 
    We have references to these three blocks as head, 
    second and third 

    llist.head	 second			 third 
        |			 |				 | 
        |			 |				 | 
    +----+------+	 +----+------+	 +----+------+ 
    | 1 | None |	 | 2 | None |	 | 3 | None | 
    +----+------+	 +----+------+	 +----+------+ 
    '''

    llist.head.next = second;  # Link first node with second

    ''' 
    Now next of first Node refers to second. So they 
    both are linked. 

    llist.head	 second			 third 
        |			 |				 | 
        |			 |				 | 
    +----+------+	 +----+------+	 +----+------+ 
    | 1 | o-------->| 2 | null |	 | 3 | null | 
    +----+------+	 +----+------+	 +----+------+ 
    '''

    second.next = third;  # Link second node with the third node

    ''' 
    Now next of second Node refers to third. So all three 
    nodes are linked. 

    llist.head	 second			 third 
        |			 |				 | 
        |			 |				 | 
    +----+------+	 +----+------+	 +----+------+ 
    | 1 | o-------->| 2 | o-------->| 3 | null | 
    +----+------+	 +----+------+	 +----+------+ 
    '''
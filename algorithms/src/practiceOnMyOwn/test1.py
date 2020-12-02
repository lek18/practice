class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class linklist:
    def __init__(self):
        self.headval = None
    def printlist(self):
        current = self.headval
        while current is not None:
            print(current.dataval)
            current = current.nextval

    def reverse_link_list(self):
        current = self.headval
        previous = None
        while current is not None:
            next = current.nextval # let store the following node so we can reverse in the following iteration

            current.nextval = previous #  this is the swap - make previous next
            previous = current # make previous current!

            current = next # this for the following node
        self.head = previous




# these are my nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
# link my nodes
node1.nextval=node2
node2.nextval=node3
node3.nextval=node4
node4.nextval=node5

# node5.nextval = node4
# node4.nextval = node3
# node3.nextval = node2
# node2.nextval = node1
# head = node 5

#make the link list
mylink_list = linklist()
mylink_list.headval = node1
mylink_list.printlist()


# a = range(0,5)
# b = list(map(lambda x:Node(x),a))
#Find duplicates
# given array of size n, elements include 1 to n-1
def findDuplicates(list_ints):
    #Lets define two animals - hare and tortois
    tortoise = list_ints[0]
    hare = tortoise

    while True:
        tortoise = list_ints[tortoise]
        hare = list_ints[list_ints[hare]]
        if tortoise==hare:
            break

    pt1 = list_ints[0]
    pt2 = tortoise

    while pt1!=pt2:
        pt1 = list_ints[pt1]
        pt2 = list_ints[pt2]
    return pt1

findDuplicates([10,9,2,3,2,4,5,8,6,7,1])

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class llist:
    def __init__(self):
        self.head = None

    def printlist(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    def pushNode(self,new_data):
        newNode = Node(new_data)
        newNode.next = self.head
        self.head = newNode

    def reverseList(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next # save current value
            current.next = prev # swtich the place of prev
            prev = current
            current = next
        self.head = prev # start from the last

a = [1,2,3,4]
mylink_list = llist()
list(map(lambda x: mylink_list.pushNode(x),a[::-1]))

a1 = [4,5,6,7]
mylink_list2 = llist()
list(map(lambda x: mylink_list2.pushNode(x),a1[::-1]))

mylink_list2.printlist()

mylink_list.reverseList()

def merge2SortedList(h1,h2):
    #case is one or the other is none return the other that isnt
    if (h1 == None):
        return h2
    if (h2 == None):
        return h1

    # lets choose the largest head and start from there
    if (h1.data<h2.data):
        h1.next = merge2SortedList(h1.next,h2)
        return h1
    else:
        h2.next = merge2SortedList(h1, h2.next)
        return h2

new_head = merge2SortedList(mylink_list.head,mylink_list2.head)
my_merge_list = llist()
my_merge_list.head=new_head
my_merge_list.printlist()

mylink_list.printlist()
mylink_list2.printlist()
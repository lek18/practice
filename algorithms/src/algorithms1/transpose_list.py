
def transpose(matrix):
    output = []
    number_of_cols = len(matrix[0]) #ie num of rows become nums of cols
    for i in range(number_of_cols):
        dummy_col = []
        for row in matrix:
            dummy_col = dummy_col + [row[i]]
        output = output + [dummy_col]

    return output

matrix = [[1,2,3],[4,5,6]]
transpose(matrix)

def findDuplicates(array):
    size = len(array)
    output = []
    for i in range(size):
        if array[abs(array[i])]>=0:
            array[abs(array[i])] = -array[abs(array[i])]
        else:
            output = output + [abs(array[i])]
            print(abs(array[i]))
    return output
arr = [1,1, 2, 3, 2, 3, 6, 4]
findDuplicates(arr)
# reverse a link list

class Node:
    def __init__(self,data_value):
        self.data_val = data_value
        self.next = None

class LList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        print(current)
        while current is not None:
            print(current.data_val)
            current = current.next

    def push(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
    def reverse_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    def length_list(self):
        self.counter = 0
        current = self.head
        while current is not None:
            self.counter = self.counter + 1
            current = current.next

    def push_data_end(self,values_array):
        # first reverse the list
        self.reverse_list()
        # push values to list
        for i in values_array:
            self.push(i)
        # reverse the array once more
        self.reverse_list()

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3

my_list = LList()
my_list.head = n1
my_list.print_list()
my_list.reverse_list()
my_list.print_list()
my_list.length_list()
my_list.counter


#lets add 3 zeros to the end
zero_stuff = [0]*3
my_list.push_data_end(zero_stuff)


my_values = [1,2,3,10,11,19]
ll2 = LList()
list(map(lambda x:ll2.push(x),my_values))
ll2.print_list()
ll2.reverse_list()
ll2.print_list()

## function to add two link list



def add_2_link_list(self,l1:LList,l2:LList):
    # assume number start like left to write 1234 + 5698
    # we need to reverse the two list since we will be adding right to left

    l1.reverse_list()
    l2.reverse_list()

    #Now we go line head by head adding the numbers
    current_l1 = l1.head
    current_l2 = l2.head
    remainder = 0
    my_output_list = LList()
    while current_l1 is not None or current_l2 is not None:
        cur_l1_node_value = current_l1.data_val
        cur_l1_node_value = current_l2.data_val

        # # Check if one either is NOne if they are make it 0
        # if cur_l1_node_value is None:
        #     cur_l1_node_value =

        sum_value = cur_l1_node_value+cur_l1_node_value + remainder
        if sum_value>10:
            remainder = 1
            sum_value = sum_value-10
            # my_output_list.push(sum_value)

        # Push sum value to my_output_list
        my_output_list.push(sum_value)
        current_l1 = current_l1.next
        current_l2 = current_l2.next

import math


# Add any extra import statements you may need here


class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Add any helper functions you may need here


def reverse(head):
    # Write your code here

    newNode = Node(1)
    newNode.next = head

    if head.data%2!=0:
        current = newNode.next
    else:
        current = newNode

    while current:
        if current.data % 2 != 0 and current.next and current.next.data%2==0:
                prev = None

                start = current.next

                start_head = start

                while start and start.data % 2 == 0:
                    next = start.next
                    start.next = prev
                    prev = start
                    start = next

                start_head.next = start
                current.next = prev
                current = start
        else:
            current = current.next

    return newNode.next


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printLinkedList(head):
    print('[', end='')
    while head != None:
        print(head.data, end='')
        head = head.next
        if head != None:
            print(' ', end='')
    print(']', end='')


test_case_number = 1


def check(expectedHead, outputHead):
    global test_case_number
    tempExpectedHead = expectedHead
    tempOutputHead = outputHead
    result = True
    while expectedHead != None and outputHead != None:
        result &= (expectedHead.data == outputHead.data)
        expectedHead = expectedHead.next
        outputHead = outputHead.next

    if not (outputHead == None and expectedHead == None):
        result = False

    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, ' Test #', test_case_number, sep='')
    else:
        print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
        printLinkedList(tempExpectedHead)
        print(' Your output: ', end='')
        printLinkedList(tempOutputHead)
        print()
    test_case_number += 1


def createLinkedList(arr):
    head = None
    tempHead = head
    for v in arr:
        if head == None:
            head = Node(v)
            tempHead = head
        else:
            head.next = Node(v)
            head = head.next
    return tempHead


if __name__ == "__main__":
    head_1 = createLinkedList([1, 2,4,6,8,10])
    expected_1 = createLinkedList([1,10,8,6,4,2])
    output_1 = reverse(head_1)
    check(expected_1, output_1)

    head_2 = createLinkedList([1, 2, 3, 3, 4, 6, 8, 5])
    expected_2 = createLinkedList([1, 2, 3, 3, 8, 6, 4, 5])
    output_2 = reverse(head_2)
    check(expected_2, output_2)

    # Add your own test cases here

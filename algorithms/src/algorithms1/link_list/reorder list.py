# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return head

        current = head
        head = current

        while current:
            current_next = current.next
            # print(head)
            # loop to the end starting from current

            node = current
            # print("current",current)
            while node.next:
                prev = node
                node = node.next
                # print("prev",prev.val)
                # print("next",node.val,node.next)
            # current = current_next
            # prev, node will be of the form. N1 --> N2 --> NONE
            # make prev point to None since N2 will be popped
            if prev == current:
                return head
            prev.next = None
            current.next = node
            node.next = current_next
            current = current_next
            # print(head)

        return head

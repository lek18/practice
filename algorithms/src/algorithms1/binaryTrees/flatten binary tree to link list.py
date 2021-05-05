# O(N) space O(1)
class Solution:

    def flatten(self, root: "TreeNode") -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Handle the null scenario
        if not root:
            return None

        node = root
        while node:

            # If the node has a left child
            if node.left:

                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right

                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None

            # move on to the right side of the tree
            node = node.right

# O(N) and O(N)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        if root is None:
            return None

        current = root

        left = [current.left]
        right = [current.right]
        # current.left = None
        while left or right:
            # pop from the left side
            val = left.pop() if left else right.pop()
            # if val is a Node, then append it to current.left
            if val:
                # save the contents of val respectively
                left.append(val.left)
                right.append(val.right)
                current.right = val
                current.left = None
                current = current.right



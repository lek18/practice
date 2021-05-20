# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def helper_func(self, start):

        L = start.left if start else None
        R = start.right if start else None
        if L is None and R is None:
            self.count_val += 1
            return 1
        is_uni = 1
        if L:
            is_uni = self.helper_func(L) and is_uni and L.val == start.val
        if R:
            is_uni = self.helper_func(R) and is_uni and R.val == start.val

        self.count_val += is_uni
        return is_uni

    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.count_val = 0

        self.helper_func(root)

        return self.count_val
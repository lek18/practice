class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_gain(node):
            global max_sum
            if not node:
                return 0

            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain

            # update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_newpath)

            # for recursion :
            # return the max gain if continue the same path
            # print(node.val, max(left_gain, right_gain),max_sum)
            return node.val + max(left_gain, right_gain)  # [node.val,max(left_gain, right_gain)]

        global max_sum
        max_sum = float('-inf')
        max_gain(root)
        return max_sum
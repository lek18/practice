class Solution:
    def inorderTraversal(self, root):
        #
        ## iteration
        stack,res = [],[]
        node = root
        # why we need to judge the node or the stack at the same time?
        # Because we will stop the first while loop when it reach the far-right leaf.
        # However, the stack will be empty when the node reaches the root.
        # And the node will be None when we reach the left leaf.
        # To make sure the node reaches the far-right leaf, we need to check the node and stack
        # in the first while loop.
        while node or stack:
            while node: # put all left nodes in the stack
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            # change the direction to the right direction after the left.children
            # and parent are taken care of, which the inorder means.
            node = node.right
        return res
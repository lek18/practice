

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Solution(object):
    def postorderTraversal(self, root):
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)

        return output[::-1]


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("\nPostorder traversal of binary tree is")
    s = Solution()
    print(s.postorderTraversal(root))
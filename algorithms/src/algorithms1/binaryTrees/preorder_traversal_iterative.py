
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class Solution(object):
    def preorderTraversal(self, root):
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)

        return output


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Function call
    print("\nPreorder traversal of binary tree is")
    s = Solution()
    print(s.preorderTraversal(root))
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self,root=None):
        self.root = Node(root)

    def print_tree(self,type):
        if type=="preorder":
            print(self.pre_orderTraversal(start = self.root,traversal =""))
        elif type =="inorder":
         print(self.in_orderTraversal(start = self.root, traversal=""))
        elif type == "postorder":
         print(self.post_orderTraversal(start=self.root, traversal=""))
        else:
            print("Type no supported")

    def pre_orderTraversal(self,start, traversal):
        # Root - Left - Right order
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.pre_orderTraversal(start.left,traversal)
            traversal = self.pre_orderTraversal(start.right,traversal)
        return traversal

    def in_orderTraversal(self,start, traversal):
        # Left Root Right order
        if start:
            traversal = self.in_orderTraversal(start.left,traversal)
            traversal += str(start.data) + "-"
            traversal = self.in_orderTraversal(start.right, traversal)
        return traversal

    def post_orderTraversal(self,start, traversal):
        # Left Right Root order
        if start:
            traversal = self.in_orderTraversal(start.left,traversal)
            traversal = self.in_orderTraversal(start.right, traversal)
            traversal += str(start.data) + "-"
        return traversal

    #insert functions
    def insert(self,data):
        #print(self.root)
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self,data, current_node):
        if data<current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data,current_node.left)
        elif data>current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data,current_node.right)
        else:
            print("Data already in Tree")

    #search functions
    def search(self,data):
        return self._search(data,self.root)

    def _search(self,data, current_node):
        #print(data)
        #print(current_node.data)
        if current_node.data == data:
            return True
        elif data>current_node.data and current_node.right is not None:
            return self._search(data, current_node.right)
        elif data<current_node.data  and current_node.left  is not None:
            return self._search(data,current_node.left)
        else:
            return False
    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(current_node=self.root)
    def _height(self,current_node):
        if current_node is None:
            return -1
        left_height = self._height(current_node=current_node.left)
        right_height = self._height(current_node=current_node.right)
        print(1 + max(left_height,right_height))
        return 1 + max(left_height,right_height)
    def checkBST(self,current_node):
        if current_node is None:
            return False
        else:
            return self._checkBST(current_node= current_node)
    # def  _checkBST(self,current_node):
    #     if current_node.left is not None and current_node.right is not None:
    #         if current_node.left.val < current_node.val and current_node.right.val>current_node.val:
    #             self._checkBST(current_node.left)
    #             self._checkBST(current_node.right)
    #     elif current_node.left is not None and
#      5
#  3       8
#2  4    6  7

myTree = BinaryTree(root = 5)
##left
myTree.root.left = Node(3)
myTree.root.left.left = Node(2)
myTree.root.left.right = Node(4)
##right
myTree.root.right = Node(8)
myTree.root.right.left = Node(6)
myTree.root.right.right = Node(7)

myTree.print_tree(type="preorder")
myTree.print_tree(type="inorder")
myTree.print_tree(type="postorder")

myTree2 = BinaryTree(root=5)
data_vals = [5,3,8,2,4,6,7]
for i in data_vals:
    myTree2.insert(data=i)

print("trying inser methods")
myTree2.print_tree(type="preorder")
myTree2.print_tree(type="inorder")
myTree2.print_tree(type="postorder")

print(myTree.search(data=2))
print(myTree.height())
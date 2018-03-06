"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

__author__ = "Wangdu Lin"
__copyright__ = "Copyright 2018, The Algorithm Project"
__credits__ = ["Wangdu Lin, jiuzhang"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wangdu Lin"
__email__ = "wangdu1005@gmail.com"
__status__ = "Production"

class Solution:
    """
    @param: root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    tree = []
    # Solution 1: Recursive
    # def inorderTraversal(self, root):
    #     # write your code here
    #     if root:
    #         self.inorderTraversal(root.left)
    #         self.tree.append(root.val)
    #         self.inorderTraversal(root.right)
        
    #     print(self.tree)
    #     return self.tree
    
    # Solution 2: Iterative
    def inorderTraversal(self, root):
        self.inorderIterative(root)
        return self.tree
        
    def inorderIterative(self, root):
        stack = []
        
        while root or stack:
            if root:
                # Step1. insert node to the stack
                stack.append(root)
                root = root.left
            else:
                # Step2. pop out the node and insert 
                # node by new order (inorder) to the self.tree
                root = stack.pop()
                self.tree.append(root.val)
                root = root.right
        return self.tree
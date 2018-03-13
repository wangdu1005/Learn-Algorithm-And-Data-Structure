__author__ = "Wangdu Lin"
__copyright__ = "Copyright 2018, The Algorithm Project"
__credits__ = ["Wangdu Lin, jiuzhang"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wangdu Lin"
__email__ = "wangdu1005@gmail.com"
__status__ = "Production"

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    tree = []
    
    # Solution1: Traversal
    # def preorderTraversal(self, root):
    #     if root:
    #         self.tree.append(root.val)
    #         self.preorderTraversal(root.left)
    #         self.preorderTraversal(root.right)
        
    #     return self.tree
        
        
    # Solution2: Iterative
    def preorderTraversal(self, root):
        self.preorderIterative(root)
        return self.tree
        
    def preorderIterative(self, root):
        stack = []
        
        while root or stack:
            if root:
                self.tree.append(root.val)
                stack.append(root)
                root = root.left
            else:
                # the node stay in the stack is for checking the tree's node's right
                root = stack.pop()
                root = root.right
                
        return self.tree
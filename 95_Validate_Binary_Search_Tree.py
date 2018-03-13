__author__ = "Wangdu Lin"
__copyright__ = "Copyright 2018, The Algorithm Project"
__credits__ = ["jiuzhang, Wangdu Lin"]
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
    @param: root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    
    def isValidBST(self, root):
        self.lastVal = None
        self.isBST = True
        
        self.validate(root)
        return self.isBST
        
    def validate(self, root):
        if root is None:
            return
        
        self.validate(root.left)
        
        if self.lastVal is not None and self.lastVal >= root.val:
            self.isBST = False
            return
        
        self.lastVal = root.val

        self.validate(root.right)
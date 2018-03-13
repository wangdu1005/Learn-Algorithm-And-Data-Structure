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
        this.val = val
        this.left, this.right = None, None
"""

class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: 
    """
    def flatten(self, root):
        # the stop condition
        if root is None:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)
        
        # root pass it's memory address to p, therefore, they hold the same address
        p = root
        
        if p.left is None:
            return
        """
        In order to focus on dealing the left node, so current p move to the p.left. Right now p has different address with root.
        """
        p = p.left

        # print(id(root))
        """
        This while loop is tring to move the current node to the end of the root.left's bottom right node.
        """
        while p.right:
            p = p.right

        """
        This p var is holding the root.left, or if p.right is not None then holding root.left.right....right.right.right, which means it depend on above statement.
        """
        p.right = root.right
        root.right = root.left 
        root.left = None
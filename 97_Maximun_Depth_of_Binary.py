"""

Time:  O(n)
Space: O(h), h is height of binary tree

This problems easy but hard to understand. I finally figure out the logic by drawing the tree graphic.
Reference: https://github.com/kamyu104/LeetCode/blob/master/Python/maximum-depth-of-binary-tree.py

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
    @param root: The root of binary tree.
    @return: An integer
    """ 
    
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
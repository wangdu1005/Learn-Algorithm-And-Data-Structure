"""

This problems easy but hard to understand. I finally figure out the logic by drawing the tree graphic.
Reference: https://github.com/kamyu104/LeetCode/blob/master/Python/maximum-depth-of-binary-tree.py

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
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
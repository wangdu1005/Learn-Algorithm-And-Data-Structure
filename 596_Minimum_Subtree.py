#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    @param: root: the root of binary tree
    @return: the root of the minimum subtree
    """
    min_sum, node = sys.maxsize, None
    
    def findSubtree(self, root):
        # write your code here
        # print(self.min_sum)
        
        self.helper(root)
        return self.node
    
    def helper(self, root):
        
        if root is None:
            return 0
        
        # divide
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        
        #conquer
        sum = left_sum + right_sum + root.val
        
        if self.node is None or sum < self.min_sum:
            self.min_sum = sum
            self.node = root
        return sum
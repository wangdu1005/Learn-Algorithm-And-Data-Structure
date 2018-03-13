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
lintcode 597
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

class Solution:
    """
    @param: root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    average, node = 0, None
    
    def findSubtree2(self, root):
        # write your code here
        self.helper(root)
        return self.node
        
    def helper(self, root):
        
        if root is None:
            return 0, 0
            
        # Divide
        left_sum, left_size = self.helper(root.left)
        right_sum, right_size = self.helper(root.right)
        
        # Conquer
        sum = left_sum + right_sum + root.val
        size = left_size + right_size + 1
        
        print("sum = ", sum)
        print("size = ", size)
        
        if self.node is None or sum * 1.0 / size > self.average:
            self.node = root
            self.average = sum * 1.0 / size
            
        return sum, size
"""
Time:  O(n)
Space: O(h), h is height of binary tree

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
    @param: root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    # Solution 1: Not recommand, because single return value with multiple meaning.
    # def isBalanced(self, root):
    #     if self.getHeight(root) >= 0:
    #         return True
    #     else:
    #         return False
        
        
    # def getHeight(self, root):
    #     if root is None:
    #         return 0
    #     else:
    #         left_height, right_height = self.getHeight(root.left), self.getHeight(root.right)
            
    #         if left_height < 0 or right_height < 0 or abs(left_height - right_height) > 1:
    #             return -1
            
    #         return max(left_height, right_height) + 1

    # Solution 2: Recommand, because tuple is more clear to express the algorithm logic.
    def isBalanced(self, root):
        result, _ = self.validate(root)
        return result

    def validate(self, root):
        if root is None:
            return True, 0

        left_balan, left_height = self.validate(root.left)
        if not left_balan:
            return False, 0
            
        right_balan, right_height = self.validate(root.right)
        if not right_balan:
            return False, 0
            
        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1
    
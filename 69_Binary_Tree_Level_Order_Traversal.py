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
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    
    # Solution1:
    def levelOrder(self, root):
        result = []
        if root is None:
            return result
            
        q = [root]
        while len(q) > 0:
            level = []
            for _ in range(len(q)):
                head = q.pop(0)
                level.append(head.val)
                
                if head.left:
                    q.append(head.left)
                    
                if head.right:
                    q.append(head.right)
        
            result.append(level)
            
        return result
        
    # Solution2: Double queue variable with 3 loop (1 while, 2 for loop)
    # def levelOrder(self, root):
    #     result = []
    #     if root is None:
    #         return result
            
    #     q = [root]
    #     while len(q) > 0:
    #         new_q = []
    #         # The first for loop
    #         result.append([n.val for n in q])
            
    #         # The second for loop
    #         for node in q:
    #             if node.left:
    #                 new_q.append(node.left)
    #             if node.right:
    #                 new_q.append(node.right)
    #         q = new_q
    #     return result
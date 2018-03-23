__author__ = "Wangdu Lin"
__copyright__ = "Copyright 2018, The Algorithm Project"
__credits__ = ["Wangdu Lin, jiuzhang"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wangdu Lin"
__email__ = "wangdu1005@gmail.com"
__status__ = "Production"

"""
Time Complexity: O(n)
Space Complexity: O(n)

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    count = 0
    index = 0
    def kthSmallest(self, root, k):
        self.findK(root, k)
        return self.index

    # Return K node
    def findK(self, node, k):
        if node is None:
            return None

        self.findK(node.left, k)
        
        self.count += 1
        if self.count == k:
            self.index = node.val
        
        # We must save more time, therefore, we only keep finding right node if index still smaller than k.
        # We will return answer if index == k, so index will never have chance to bigger than k.
        if self.index < k:
            self.findK(node.right, k)
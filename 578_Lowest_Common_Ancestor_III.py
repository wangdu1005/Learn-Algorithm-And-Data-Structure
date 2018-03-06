"""

My solution on stack overflow:
https://stackoverflow.com/questions/33723034/python-find-lowest-common-ancestor-of-two-nodes-in-a-binary-tree-if-not-all-of-t/49134813#49134813

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
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
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    count = 0

    def lowestCommonAncestor3(self, root, A, B):
        result = self.lca(root, A, B)
        return result if self.count == 2 else None
        
    def lca(self, root, A, B):
        if not root:
            return None

        for node in [A, B]:
            if root == node:
                self.count += 1

        left = self.lca(root.left, A, B)
        right = self.lca(root.right, A, B)

        if root in (A, B) or left and right:
            return root
            
        if left:
            return left
        
        if right:
            return right
        
        return None
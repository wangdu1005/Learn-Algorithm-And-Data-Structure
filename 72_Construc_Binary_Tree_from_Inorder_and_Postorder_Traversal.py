"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.helper(inorder, 0, len(inorder)-1, postorder, 0, len(postorder)-1)
        
    def helper(self, inorder, ileft, iright, postorder, pleft, pright):
        if ileft > iright: return None
        if ileft == iright: return TreeNode(inorder[ileft])
        inx = inorder.index(postorder[pright])
        left_len = inx - ileft
        root = TreeNode(postorder[pright])
        root.left = self.helper(inorder, ileft, inx-1, postorder, pleft, pleft+left_len-1) 
        root.right = self.helper(inorder, inx+1, iright, postorder, pleft+left_len, pright-1)
        return root
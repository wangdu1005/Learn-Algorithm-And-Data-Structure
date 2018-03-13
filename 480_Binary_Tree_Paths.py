__author__ = "Wangdu Lin"
__copyright__ = "Copyright 2018, The Algorithm Project"
__credits__ = ["Wangdu Lin, jiuzhang"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Wangdu Lin"
__email__ = "wangdu1005@gmail.com"
__status__ = "Production"

"""

The same time complexity as in the Java version of jiuzhang. 
The current Java version is better than the python version. 
So I used java version's idea to rewritten python solution.

============================================================

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    
    def binaryTreePaths(self, root):
        paths = []
        
        if root is None:
            return paths
        
        # divide
        left_paths = self.binaryTreePaths(root.left)
        right_paths = self.binaryTreePaths(root.right)
        
        for path in left_paths:
            paths.append(str(root.val) + "->" + path)
            # print(paths)
        for path in right_paths:
            paths.append(str(root.val) + "->" + path)
        
        # count array elements
        if len(paths) == 0:
            paths.append("" + str(root.val))
        
        return paths
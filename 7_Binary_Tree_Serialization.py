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
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):    
        if root is None:
            return "{}"
            
        result = [root.val]
        q = collections.deque([root])
        while q:
            curr = q.popleft()

            if curr.left is not None:
                q.append(curr.left)

            result.append(curr.left.val if curr.left is not None else None)
            
            if curr.right is not None:
                q.append(curr.right)
            
            result.append(curr.right.val if curr.right is not None else None)
            
        # Make sure the last element (leaf node) in result is not None,
        # becasue we know leaf has two None child.
        # So we loop the last index, if it is None then we remove it. 
        while result[-1] is None:
            result.pop()
        
        def transform(val):
            if val is None:
                return "#"
            else:
                return str(val)
        
        return '{' + ','.join(map(transform, result)) + '}'
        
    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        if data == '{}':
            return None
        
        vals = data[1:-1].split(',')
        nodes = collections.deque([None if o is None else TreeNode(o) for o in vals])
        q = collections.deque([nodes.popleft()]) if nodes else None
        root = q[0] if q else None
        while q:
            parent = q.popleft()
            left = nodes.popleft() if nodes else None
            right = nodes.popleft() if nodes else None
            parent.left, parent.right = left, right
            if left:
                q.append(left)
            if right:
                q.append(right)

        return root
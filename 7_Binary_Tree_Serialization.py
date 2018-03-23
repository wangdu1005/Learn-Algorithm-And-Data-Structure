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
        # 1.Check input status
        if root is None:
            return "{}"
        
        # 2.Transform Treenode into list by using while loop
        result = [root.val]
        q = collections.deque([root])
        while q:
            curr = q.popleft()
            
            if curr.left is not None:
                q.append(curr.left)
            
            if curr.right is not None:
                q.append(curr.right)
            
            result.append(curr.left.val if curr.left is not None else None)
            result.append(curr.right.val if curr.right is not None else None)
            
        # 3.From upper code to insert val to the list which will append extra None value at the end of leaf node,
        # so must remove it, in order to make right string output.
        while result[-1] is None:
            result.pop()

        # 4.Transform list into string format, None value will be "#"
        # 5.Then Return string
        def transform(val):
            if val is None:
                return "#"
            else:
                return str(val)
        
        return "{" + ",".join(map(transform, result)) + "}"
        
    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        # 1.Check None situation
        if data == "{}":
            return None
            
        # 2.Transform string to list
        rawData = data[1:-1].split(",")
        print(data)
        
        # 3.Transform list to queue
        nodes = collections.deque([TreeNode(val) if val != "#" else None for val in rawData])
        print(nodes)
        
        q = collections.deque([nodes.popleft()])
        # 4.Assign the reference of first node to root variable, not copy it.
        root = q[0]
        
        # 5.while loop the queue by BFS and popleft the nodes deque
        while q:
            parent = q.popleft()
            left = nodes.popleft() if len(nodes) > 0 else None
            right = nodes.popleft() if len(nodes) > 0 else None
            parent.left, parent.right = left, right
            
            if left is not None:
                q.append(left)
                
            if right is not None:
                q.append(right)
                
        return root
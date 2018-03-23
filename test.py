class Solution:
    def ans(self, node, k):
        nodeK = self.findK(node, k)
        return nodeK

    findK = 1
    # Return K node
    def findK(self, node, k):
        if node is None:
            return None

        left = findK(node.left)
        if self.findK == k:
            return node
        else:
            self.findK += 1
        findK(node.right)
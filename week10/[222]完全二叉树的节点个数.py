class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        left = self.countNodes(root.left)
        right= self.countNodes(root.right)
        return left+right+1
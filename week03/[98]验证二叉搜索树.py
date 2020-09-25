# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。 
# 
#  假设一个二叉搜索树具有如下特征： 
# 
#  
#  节点的左子树只包含小于当前节点的数。 
#  节点的右子树只包含大于当前节点的数。 
#  所有左子树和右子树自身必须也是二叉搜索树。 
#  
# 
#  示例 1: 
# 
#  输入:
#     2
#    / \
#   1   3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
#     5
#    / \
#   1   4
#      / \
#     3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
#      根节点的值为 5 ，但是其右子节点值为 4 。
#  
#  Related Topics 树 深度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        def isBST(root, lowerLimit, upperLimit):
            if root == None:
                return True
            if root.val <= lowerLimit or root.val >= upperLimit:
                return False
            # 左子数 要比根结点小 且整个左子树的元素都小于它的上界
            # 右子树 要比根结点大，且整个右子树的元素都大于它的下界
            return isBST(root.left, lowerLimit, root.val) and isBST(root.right, root.val, upperLimit)

        return isBST(root, -float("inf"), float("inf"))

# 时间复杂度 : O(N)O(N)。每个结点访问一次。
# 空间复杂度 : O(N)O(N)。我们跟进了整棵树

        # def recur(root, lower, upper):
        #     if not root: return True
        #
        #     if root.val <= lower: return False
        #     if root.val >= upper: return False
        #
        #     return recur(root.left, lower, root.val) and recur(root.right, root.val, upper)
        #
        # return recur(root, float("-inf"), float("inf"))
# leetcode submit region end(Prohibit modification and deletion)

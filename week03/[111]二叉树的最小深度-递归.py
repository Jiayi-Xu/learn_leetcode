# 给定一个二叉树，找出其最小深度。 
# 
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 
# 
#  说明: 叶子节点是指没有子节点的节点。 
# 
#  示例: 
# 
#  给定二叉树 [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7 
# 
#  返回它的最小深度 2. 
#  Related Topics 树 深度优先搜索 广度优先搜索


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        递归方案：
        当 root 节点左右孩子都为空时，返回 1
        当 root节点左右孩子只有一个为空，说明root节点不是叶子节点，那此时的最小深度就是不为空的那棵子树的最小深度+1
        当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值
        """

        if not root: return 0

        # 当 root 节点左右孩子都为空时，返回 1
        if not root.left and not root.right: return 1

        # 当 root节点左右孩子只有一个为空，说明root节点不是叶子节点
        #  此时的最小深度就是不为空的那棵子树的最小深度+1
        if not root.left or not root.right:
            return 1 + max(self.minDepth(root.left), self.minDepth(root.right))

            # 当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1




        # if not root: return 0
        #
        # children = [root.left, root.right]
        # # 没有叶子结点
        # if not any(children):
        #     return 1
        # depth = float('inf')
        # for child in children:
        #     if child:
        #         depth = min(self.minDepth(child), depth)
        #
        # return depth + 1


# leetcode submit region end(Prohibit modification and deletion)

# 给定一个二叉树，返回它的 前序 遍历。 
# 
#  示例: 
# 
#  输入: [1,null,2,3]  
#    1
#     \
#      2
#     /
#    3 
# 
# 输出: [1,2,3]
#  
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 
#  👍 368 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        """
        递归方案：执行耗时:16 ms,击败了87.91% 的Python用户
        """
        # if not root:
        #     return []
        #
        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)


        """
        迭代方案：执行耗时:20 ms,击败了67.29% 的Python用户
        先将根节点放入栈中,然后将其弹出,依次压入弹出节点的右节点,和左节点
        """

        if not root:
            return []

        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            ans.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ans


# leetcode submit region end(Prohibit modification and deletion)

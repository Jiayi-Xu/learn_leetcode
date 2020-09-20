# 给定一个二叉树，返回它的中序 遍历。 
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
# 输出: [1,3,2] 
# 
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？ 
#  Related Topics 栈 树 哈希表 
#  👍 711 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        """
        递归方案：执行耗时:20 ms,击败了67.63% 的Python用户
        """

        # if not root:
        #     return []
        # return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


        """
        迭代方案：执行耗时:20 ms,击败了67.63% 的Python用户
        
        用栈来存储的解决方案
        先建立一个栈。一个一个往里存，先访问左边子节点。如果是空，就把栈顶的点输出出来。
        先用指针找到每颗子树的最左下角，然后进行进出栈操作
        
        
        例子： 【A, B, C, D, E, F, null]
        
                    A
            B               C
        D      E        F
        中序遍历：DBEAFC
        栈的变化：
        D
        B   B   E       F
        A   A   A   A   C   C   出栈完毕
        """
        if not root:
            return []

        node = root
        stack = []
        ans = []

        while stack or node:
            while node:
                # 压入结点
                stack.append(node)
                # 不断访问左边子节点。如果是空说明到达最左边，就跳出循环开始把栈顶的点输出出来
                node = node.left

            # 弹出栈顶的值
            node = stack.pop()
            ans.append(node.val)
            # 开始访问右子树
            node = node.right
        return ans




# leetcode submit region end(Prohibit modification and deletion)

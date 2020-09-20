# 给定一个 N 叉树，返回其节点值的前序遍历。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其前序遍历: [1,3,5,6,2,4]。 
# 
#  
# 
#  说明: 递归法很简单，你可以使用迭代法完成此题吗? Related Topics 树 
#  👍 102 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        """
        方案一：递归方案 执行耗时:48 ms,击败了46.69% 的Python用户
        """
        # res = []
        # def traversal(root):
        #     if not root:
        #         return []
        #     res.append(root.val)
        #     for child in root.children:
        #         traversal(child)
        #
        # traversal(root)
        # return res

        """
        方案二：迭代方案 执行耗时:40 ms,击败了81.39% 的Python用户
        """

        if not root:
            return

        res = []
        stack = [root]

        while stack:
            # 当栈有结点时提取结点
            node = stack.pop()
            res.append(node.val)

            # 用for循环 执行耗时:48 ms,击败了46.69% 的Python用户
            # for child in node.children[::-1]:
            #     stack.append(child)
            # 倒序插入stack再顺序pop出来
            stack.extend(node.children[::-1])
        return res

# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/solution/589ncha-shu-de-qian-xu-bian-li-by-821218213/
# leetcode submit region end(Prohibit modification and deletion)

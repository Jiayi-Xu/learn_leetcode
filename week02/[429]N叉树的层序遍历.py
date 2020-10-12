# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。 
# 
#  例如，给定一个 3叉树 : 
# 
#  
# 
#  
# 
#  
# 
#  返回其层序遍历: 
# 
#  [
#      [1],
#      [3,2,4],
#      [5,6]
# ]
#  
# 
#  
# 
#  说明: 
# 
#  
#  树的深度不会超过 1000。 
#  树的节点总数不会超过 5000。 
#  Related Topics 树 广度优先搜索 
#  👍 109 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
import collections


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """

        if not root:
            return []

        queue = collections.deque([root])
        res = []

        # 当队列还有数据时
        while queue:
            size = len(queue)
            tmp = []
            # 按层提取
            for _ in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                queue.extend(node.children)

            res.append(tmp)

        return res

        
# leetcode submit region end(Prohibit modification and deletion)

"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        ans = []
        level = 0
        while queue:

            tmp_size = len(queue)
            ans.append([])
            for i in range(tmp_size):
                node = queue.pop(0)
                ans[level].append(node.val)
                queue.extend(node.children[:])
            level += 1
        return ans
"""
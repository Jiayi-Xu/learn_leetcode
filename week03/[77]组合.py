# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法 
#  👍 400 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        if k <= 0 or n < k:
            return res
        def dfs(start, n, k, lst):
            if len(lst) == k:
                res.append(lst[:])
                return

            # 搜索起点的上界 = n - (k - len(lst)) + 1 优化进行剪枝
            for i in range(start, n+2-k+len(lst)):
                lst.append(i)
                # print(lst)
                dfs(i+1, n, k, lst)
                lst.pop()
        dfs(1, n, k, [])

        return res
# leetcode submit region end(Prohibit modification and deletion)

# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。 
# 
#  说明：每次只能向下或者向右移动一步。 
# 
#  示例: 
# 
#  输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#  
#  Related Topics 数组 动态规划 
#  👍 703 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # DP方程
        # dp[i][j] = min(dp[i-1][j], dp[i][j-1])
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])

        dp = grid
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i - 1][0]

        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        # print(dp)
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)

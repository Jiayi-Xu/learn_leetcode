# 给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。 
# 
#  例如，给定三角形： 
# 
#  [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#  
# 
#  自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。 
# 
#  说明： 
# 
#  如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。 
#  Related Topics 数组 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        从三角形的底层往上进行修改。从倒数第二层开始往上遍历各层，
        对某一层来说，从头开始修改这一层的所有元素，
        计算每个结点加上左右子结点（子路径）中较小的值，并放入当前结点。
        逐层修改，直到第一层，当修改完第一层之后，
        第一层的（节点）元素就是我们要求的最小路径和。
        """
        n = len(triangle)
        lst = triangle[-1]

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                lst[j] =min(lst[j],lst[j+1]) + triangle[i][j]

        #print(lst[0])
        return(lst[0])
# leetcode submit region end(Prohibit modification and deletion)

"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row = len(triangle)
        dp = triangle

        # sub(i,j) = min(sub(i+1,j), sub(i+1,j+1)) + a[i,j]
        for i in range(row-2, -1, -1):
            # 对应第i行列数
            for j in range(len(triangle[i])):
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])

        return dp[0][0]
"""
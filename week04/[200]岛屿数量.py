# 给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设
# 网格的四个边均被水包围。 
# 
#  示例 1: 
# 
#  输入:
# 11110
# 11010
# 11000
# 00000
# 
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入:
# 11000
# 11000
# 00100
# 00011
# 
# 输出: 3
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """


        if not grid:
            return 0

        row, col = len(grid), len(grid[0])

        family = 0

        def dfs(i, j):

            if i>=row or j>=col or i<0 or j<0 or grid[i][j] == '0':
                return
            # 优化可以将方向存到坐标数组里去遍历
            if grid[i][j] == '1':
                grid[i][j] = '0'
                dfs(i, j + 1)
                dfs(i + 1, j)
                dfs(i, j -1)
                dfs(i-1, j)


        for i in range(row):
            for j in range(col):
                # print("grid[i][j]  is",grid[i][j] )
                if grid[i][j] == '1':
                    family += 1
                    dfs(i, j)

        return family
# leetcode submit region end(Prohibit modification and deletion)

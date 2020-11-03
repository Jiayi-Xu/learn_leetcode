# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
# 
#  每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
# 
#  
# 
#  示例： 
# 
#  输入：4
# 输出：[
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 
#  
#  Related Topics 回溯算法 
#  👍 658 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        def dfs(queens, pie, na):
            p = len(queens)
            if p == n:
                # print(queens)
                # queens存储每行的Q的索引位置
                result.append(queens)
                return None

            for q in range(n):
                if q not in queens and p+q not in pie and p-q not in na:
                    dfs(queens+[q], pie + [p+q], na + [p-q])

        result = []
        dfs([],[],[])
        return [["."*i + "Q" + "."*(n-i-1) for i in col] for col in result]

# leetcode submit region end(Prohibit modification and deletion)


"""
        # 方案一：使用pie,na,cols集合判断重合
        def backtrack(row):
            if row == n:
                board = []
                for i in range(n):
                    row = ["."] * n
                    row[queens[i]] = "Q"
                    board.append("".join(row))
                solutions.append(board)

            else:
                for i in range(n):
                    if i in cols or row + i in pie or row - i in na:
                        continue

                    queens[row] = i
                    cols.add(i)
                    pie.add(row+i)
                    na.add(row-i)
                    backtrack(row+1)

                    cols.remove(i)
                    pie.remove(row+i)
                    na.remove(row-i)

        solutions = []
        cols = set()
        pie = set()
        na = set()
        queens = [-1] * n
        backtrack(0)
        return solutions

"""
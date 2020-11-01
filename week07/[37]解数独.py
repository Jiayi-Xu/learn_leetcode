# 编写一个程序，通过填充空格来解决数独问题。 
# 
#  一个数独的解法需遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
#  
# 
#  空白格用 '.' 表示。 
# 
#  
# 
#  一个数独。 
# 
#  
# 
#  答案被标成红色。 
# 
#  提示： 
# 
#  
#  给定的数独序列只包含数字 1-9 和字符 '.' 。 
#  你可以假设给定的数独只有唯一解。 
#  给定数独永远是 9x9 形式的。 
#  
#  Related Topics 哈希表 回溯算法 
#  👍 674 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return False
        def isValid(board, row, col, c):
            for k in xrange(9):
                # 只要行，列，block任一一个重复则返回false
                # 判断行有没有重复
                if board[row][k] != "." and board[row][k] == c: return False
                # 判断列有没有重复
                if board[k][col] != "." and board[k][col] == c: return False

                # 判断box是否重复
                box_r = (row / 3) * 3 + k / 3
                box_c = (col / 3) * 3 + k % 3
                if board[box_r][box_c] != "." and board[box_r][box_c] == c: return False

            return True

        def dfs(board):
            for i in xrange(9):
                for j in xrange(9):

                    if board[i][j] == ".":
                        # 尝试填充
                        for c in range(1, 10):
                            if isValid(board, i, j, str(c)):
                                board[i][j] = str(c)

                                if dfs(board):
                                    return True
                                else:
                                    # 恢复上一级状态
                                    board[i][j] = "."
                        return False
            return True

        dfs(board)
# leetcode submit region end(Prohibit modification and deletion)

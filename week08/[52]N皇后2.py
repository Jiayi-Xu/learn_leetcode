# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  
# 
#  上图为 8 皇后问题的一种解法。 
# 
#  给定一个整数 n，返回 n 皇后不同的解决方案的数量。 
# 
#  示例: 
# 
#  输入: 4
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#  
# 
#  
# 
#  提示： 
# 
#  
#  皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或 N
# -1 步，可进可退。（引用自 百度百科 - 皇后 ） 
#  
#  Related Topics 回溯算法 
#  👍 205 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1: return 0
        self.count = 0
        # 初始时，三个整数的值都等于 0，表示没有放置任何皇后
        self.DFS(n, 0, 0, 0, 0)
        return self.count

    def DFS(self, n, row, cols, pie, na):
        # recursion terminator
        if row >= n:
            self.count += 1
            return
        # 得到当前所有的空位
        # 三个整数的按位或运算的结果即为不能放置皇后的位置，其余位置即为可以放置皇后的位置
        availablePositions = (~(cols | pie | na)) & ((1 << n) - 1)

        # print(bin(availablePositions))
        while availablePositions:
            p = availablePositions & (-availablePositions)  # 取到最低位的1
            availablePositions = availablePositions & (availablePositions-1)  # 表示在p位置上放入皇后
            # print("p位置放皇后",bin(availablePositions))
            self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)

# leetcode submit region end(Prohibit modification and deletion)

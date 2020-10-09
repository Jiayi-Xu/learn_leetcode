# 让我们一起来玩扫雷游戏！ 
# 
#  给定一个代表游戏板的二维字符矩阵。 'M' 代表一个未挖出的地雷，'E' 代表一个未挖出的空方块，'B' 代表没有相邻（上，下，左，右，和所有4个对角线）
# 地雷的已挖出的空白方块，数字（'1' 到 '8'）表示有多少地雷与这块已挖出的方块相邻，'X' 则表示一个已挖出的地雷。 
# 
#  现在给出在所有未挖出的方块中（'M'或者'E'）的下一个点击位置（行和列索引），根据以下规则，返回相应位置被点击后对应的面板： 
# 
#  
#  如果一个地雷（'M'）被挖出，游戏就结束了- 把它改为 'X'。 
#  如果一个没有相邻地雷的空方块（'E'）被挖出，修改它为（'B'），并且所有和其相邻的未挖出方块都应该被递归地揭露。 
#  如果一个至少与一个地雷相邻的空方块（'E'）被挖出，修改它为数字（'1'到'8'），表示相邻地雷的数量。 
#  如果在此次点击中，若无更多方块可被揭露，则返回面板。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入: 
# 
# [['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'M', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E'],
#  ['E', 'E', 'E', 'E', 'E']]
# 
# Click : [3,0]
# 
# 输出: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# 解释:
# 
#  
# 
#  示例 2： 
# 
#  输入: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'M', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# Click : [1,2]
# 
# 输出: 
# 
# [['B', '1', 'E', '1', 'B'],
#  ['B', '1', 'X', '1', 'B'],
#  ['B', '1', '1', '1', 'B'],
#  ['B', 'B', 'B', 'B', 'B']]
# 
# 解释:
# 
#  
# 
#  
# 
#  注意： 
# 
#  
#  输入矩阵的宽和高的范围为 [1,50]。 
#  点击的位置只能是未被挖出的方块 ('M' 或者 'E')，这也意味着面板至少包含一个可点击的方块。 
#  输入面板不会是游戏结束的状态（即有地雷已被挖出）。 
#  简单起见，未提及的规则在这个问题中可被忽略。例如，当游戏结束时你不需要挖出所有地雷，考虑所有你可能赢得游戏或标记方块的情况。 
#  
#  Related Topics 深度优先搜索 广度优先搜索 
#  👍 184 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """

        """
        从click开始，查找各方向，如果有E计算数量，如果没有E则设置为B
        """

        row = len(board)
        col = len(board[0])

        # 八个方向
        dx = [-1, -1, -1, 0, 1, 1, 1,  0]
        dy = [-1,  0,  1, 1, 1, 0, -1, -1]


        def DFS(i, j):
            # print("i,j is",i,j, "board[i][j] is",board[i][j])
            # 判断最初点击的是否是地雷，如果是地雷则直接结束
            if i < 0 or i > row or j < 0 or j > col:
                return
            if i >= 0 and i < row and j >= 0 and j < col and board[i][j] == 'M':
                board[i][j] = 'X'
                return
            # 如果第一次点击的不是地雷，则开始遍历八个方向，统计地雷数目
            # 周边地雷为0设置为B，否则设置数量
            countM = 0
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                # DFS(x, y)
                if x >= 0 and x < row and y >= 0 and y < col:
                    if board[x][y] == 'M':
                        countM += 1
            if countM == 0:
                board[i][j] = 'B'
                # 只有为"B"的情况下再去搜索周边的
                for k in range(8):
                    x = i + dx[k]
                    y = j + dy[k]
                    if x >= 0 and x < row and y >= 0 and y < col and board[x][y] == 'E':
                        DFS(x, y)
            else:
                board[i][j] = str(countM)

        DFS(click[0], click[1])
        return board


        
# leetcode submit region end(Prohibit modification and deletion)

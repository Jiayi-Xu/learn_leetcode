# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#  
# 
#  示例: 
# 
#  输入: 
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# 
# 输出: ["eat","oath"] 
# 
#  说明: 
# 你可以假设所有输入都由小写字母 a-z 组成。 
# 
#  提示: 
# 
#  
#  你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？ 
#  如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何
# 实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。 
#  
#  Related Topics 字典树 回溯算法 
#  👍 272 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # 判断是否存在
        if not board or not board[0]: return []
        # 实现前缀树
        root = {}
        end_word = "#"

        for word in words:
            node = root
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node[end_word] = end_word

        # 实现DFS 上下左右
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        row = len(board)
        col = len(board[0])
        result = set()

        def dfs(i, j, board, path, cur_dict):
            path += board[i][j]
            cur_dict = cur_dict[board[i][j]]
            # 如果end_word在说明找到word， 否则可能只是前缀
            if end_word in cur_dict:
                result.add(path)
            # 存储board[i][j]为其它字符，避免重复使用
            tmp, board[i][j] = board[i][j], "@"
            # if i >= row or i<0 or j >= col or j < 0: return
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if 0 <= x < row and 0 <= y < col and board[x][y] != "@" and board[x][y] in cur_dict:
                    dfs(x, y, board, path, cur_dict)
            board[i][j] = tmp

        for i in range(row):
            for j in range(col):
                if board[i][j] in root:
                    dfs(i, j, board, "", root)

        return list(result)
# leetcode submit region end(Prohibit modification and deletion)

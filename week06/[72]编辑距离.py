
#
# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
# 
#  你可以对一个单词进行如下三种操作： 
# 
#  
#  插入一个字符 
#  删除一个字符 
#  替换一个字符 
#  
# 
#  示例 1: 
# 
#  输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释: 
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#  
# 
#  示例 2: 
# 
#  输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释: 
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # word1 = word1.encode('utf-8')
        # word2 = word2.encode('utf-8')
        row = len(word1)
        col = len(word2)
        dp = [[0 for _ in range(col+1)] for _ in range(row+1)]

        for i in range(1,row+1):
            dp[i][0] = i
        for j in range(1,col+1):
            dp[0][j] = j

        # 开始进行动态规划
        for i in range(1,row+1):
            for j in range(1,col+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 三种字符串操作方式
                    #替换操作 = dp[i - 1][j - 1] + 1
                    #删除操作 = dp[i - 1][j] + 1
                    #增加操作 = dp[i][j - 1] + 1
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        #print(dp)

        # i,j = row,col
        # while (i>=0 and j>=0):
        #     # 向上，删除一个字符
        #     if dp[i - 1][j] + 1 == dp[i][j]:
        #         print("删除了 {}".format(word1[i - 1]))
        #         i = i - 1
        #     # 向左回溯 增加字符
        #     elif dp[i][j - 1] + 1 == dp[i][j]:
        #         print("增加了 {}".format(word2[j - 1]))
        #         j = j - 1
        #     elif dp[i - 1][j - 1] + 1 == dp[i][j]:
        #         print("替换 {} 为 {}".format(word1[i - 1], word2[j - 1]))
        #         i = i - 1
        #         j = j - 1
        #     elif dp[i - 1][j - 1] == dp[i][j]:
        #         i = i - 1
        #         j = j - 1
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)

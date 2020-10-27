# 给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。 
# 
#  具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。 
# 
#  
# 
#  示例 1： 
# 
#  输入："abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#  
# 
#  示例 2： 
# 
#  输入："aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa" 
# 
#  
# 
#  提示： 
# 
#  
#  输入的字符串长度不会超过 1000 。 
#  
#  Related Topics 字符串 动态规划 
#  👍 425 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        dp = [[False for _ in range(length)] for _ in range(length)]
        count = 0

        for j in range(length):
            for i in range(j+1):
                # print(i,j)
                # 单个字符
                if i == j:
                    dp[i][j] = True
                    count += 1
                # 两个字符
                elif j-i == 1 and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1
                # 多余两个字符
                elif j-i > 1 and dp[i+1][j-1] == True and s[i] == s[j]:
                    dp[i][j] = True
                    count += 1


        # print(dp)
        return count




        
# leetcode submit region end(Prohibit modification and deletion)

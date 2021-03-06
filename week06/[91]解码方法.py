# 一条包含字母 A-Z 的消息通过以下方式进行了编码： 
# 
#  'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#  
# 
#  给定一个只包含数字的非空字符串，请计算解码方法的总数。 
# 
#  题目数据保证答案肯定是一个 32 位的整数。 
# 
#  
# 
#  示例 1： 
# 
#  输入："12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
#  
# 
#  示例 2： 
# 
#  输入："226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#  
# 
#  示例 3： 
# 
#  输入：s = "0"
# 输出：0
#  
# 
#  示例 4： 
# 
#  输入：s = "1"
# 输出：1
#  
# 
#  示例 5： 
# 
#  输入：s = "2"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 100 
#  s 只包含数字，并且可以包含前导零。 
#  
#  Related Topics 字符串 动态规划 
#  👍 540 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        # dp[i]表示s[:i]的编码总数
        dp = [1, 0]
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            dp.append(0)
            if s[i] != '0':
                dp[i + 1] += dp[i]
            if s[i - 1:i + 1] >= '10' and s[i - 1:i + 1] <= '26':
                dp[i + 1] += dp[i - 1]

        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)

# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划 
#  👍 1040 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        动态规划：当遇到右括号时候去查前方是否是左括号，i - dp[i-1] - 1 且该位置需要大于等于0，不然会从尾部搜索
        转移方程为 2 + dp[i-1] + dp[i - dp[i-1] -2]
        """
        if len(s) == 0: return  0
        dp = [0 for _ in s]
        for i in range(len(s)):
            if s[i] == ")" and i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == "(":
                dp[i] = 2 + dp[i-1] + dp[i - dp[i-1] -2]

        # print(dp)
        return max(dp)
# leetcode submit region end(Prohibit modification and deletion)

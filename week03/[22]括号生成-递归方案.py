# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法 
#  👍 1322 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def recursion(left, right, n, s):
            if left==n and right==n:
                res.append(s)
                return

            if left < n:
                recursion(left + 1, right, n, s +  "(")
            if left > right and right <n:
                recursion(left, right + 1, n, s +  ")")

        recursion(0, 0, n, "")

        return res
# leetcode submit region end(Prohibit modification and deletion)

# 给定两个字符串 s 和 t，它们只包含小写字母。 
# 
#  字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。 
# 
#  请找出在 t 中被添加的字母。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e' 是那个被添加的字母。
#  
# 
#  示例 2： 
# 
#  输入：s = "", t = "y"
# 输出："y"
#  
# 
#  示例 3： 
# 
#  输入：s = "a", t = "aa"
# 输出："a"
#  
# 
#  示例 4： 
# 
#  输入：s = "ae", t = "aea"
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 1000 
#  t.length == s.length + 1 
#  s 和 t 只包含小写字母 
#  
#  Related Topics 位运算 哈希表 
#  👍 165 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from collections import defaultdict
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ans = 0
        for c in s + t:
            ans ^= ord(c)
        return chr(ans)

        # dic_s = defaultdict(int)
        # dic_t = defaultdict(int)
        #
        # for ch in s:
        #     dic_s[ch] += 1
        # for ch in t:
        #     dic_t[ch] += 1
        #
        # for k, v in dic_t.items():
        #     if dic_s[k] != v:
        #         return k
# leetcode submit region end(Prohibit modification and deletion)

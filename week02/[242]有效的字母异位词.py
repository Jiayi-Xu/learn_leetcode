# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。 
# 
#  示例 1: 
# 
#  输入: s = "anagram", t = "nagaram"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: s = "rat", t = "car"
# 输出: false 
# 
#  说明: 
# 你可以假设字符串只包含小写字母。 
# 
#  进阶: 
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？ 
#  Related Topics 排序 哈希表 
#  👍 253 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 方案一：执行耗时:56 ms
        # return collections.Counter(s) == collections.Counter(t)

        # 方案二：执行耗时:44 ms 击败了63.13% 的Python用户
        # return sorted(s) == sorted(t)


        # 方案三：执行耗时:28 ms,击败了93.73% 的Python用户

        result = True
        # 使用set 去重
        set_s = set(s)
        # 先判断组成字符串的各个字符元素是否一致
        if set_s == set(t):
            for i in set_s:
                # 判断各个字符元素的数量是否一致
                if s.count(i) == t.count(i):
                    result = True
                # 如果不一致 直接返回false不用继续判断
                else:
                    return False
        else:
            result = False
        return result


# leetcode submit region end(Prohibit modification and deletion)

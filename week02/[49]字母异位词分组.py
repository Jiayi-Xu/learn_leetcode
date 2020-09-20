# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。 
# 
#  示例: 
# 
#  输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ] 
# 
#  说明： 
# 
#  
#  所有输入均为小写字母。 
#  不考虑答案输出的顺序。 
#  
#  Related Topics 哈希表 字符串 
#  👍 472 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        """
        方案一：建立数组来进行计数 再用hash进行比较
        执行耗时:56 ms,击败了61.47% 的Python用户
        """
        # Hash = {}
        # for s in strs:
        #     tmp = [0] * 26
        #     for j in s:
        #         tmp[ord(j) - ord('a')] += 1  # 关键语句，以'a'为基点来计数
        #     if tuple(tmp) not in Hash:
        #         Hash[tuple(tmp)] = [s]
        #     else:
        #         Hash[tuple(tmp)].append(s)
        #
        # return list(Hash.values())


        """
        方案二：    
        使用字典存储各字符串排序后的结果作为key, 再把属于同一个key的放到同一个key下作为value
        执行耗时:44 ms,击败了96.32% 的Python用户
        
        ''.join(sorted(s))速度比str(sorted(s)) tuple(sorted(s))执行快
        """
        # Hash = {}
        # for s in strs:
        #     key = ''.join(sorted(s))
        #
        #     # 以下这两句执行效率差不多
        #     # if not Hash.get(key):
        #     if key not in Hash:
        #         Hash[key] = [s]
        #     else:
        #         Hash[key].append(s)
        #
        # #     d[key] = d.get(key, []) + [w] 外网大神处理方式
        #
        # return list(Hash.values())


        """
        优化ifelse分支
        """
        # Hash = {}
        # for s in strs:
        #     key = ''.join(sorted(s))
        #     Hash[key] = Hash.get(key, []) + [s]
        # return list(Hash.values())

        """
        最后方案：使用defaultdict
        https://leetcode.com/problems/group-anagrams/discuss/376880/Fast-and-clean-solution-Python
        """
        dict = collections.defaultdict(list)
        for s in strs:
            dict[''.join(sorted(s))].append(s)
        return dict.values()

# leetcode submit region end(Prohibit modification and deletion)

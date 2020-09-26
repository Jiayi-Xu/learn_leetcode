# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法 
#  👍 918 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums: return res

        def dfs(nums, used, lst):
            # 循环终止条件
            if len(lst[:]) == len(nums):
                res.append(lst[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = 1
                    lst.append(nums[i])

                    dfs(nums, used, lst)

                    used[i] = 0
                    lst.pop()

        used = [0 for _ in nums]
        dfs(nums, used, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)

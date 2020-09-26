# 给定一个可包含重复数字的序列，返回所有不重复的全排列。 
# 
#  示例: 
# 
#  输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ] 
#  Related Topics 回溯算法 
#  👍 471 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums):
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
            # 设置tmp列表，存储已经使用过的元素，当下一个元素和tmp里的重复，则直接进行下一个循环
            # 或者先将数组进行排序，当nums[i] == nums[i-1]跳过循环
            tmp = []
            for i in range(len(nums)):
                if nums[i] in tmp:
                    continue
                if not used[i]:
                    used[i] = 1
                    lst.append(nums[i])

                    dfs(nums, used, lst)

                    used[i] = 0
                    lst.pop()

                    tmp.append(nums[i])

        used = [0 for _ in nums]
        dfs(nums, used, [])
        return res
# leetcode submit region end(Prohibit modification and deletion)

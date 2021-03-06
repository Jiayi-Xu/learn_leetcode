# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。 
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                # 根据值找到对应的索引位置
                return [dict[target-nums[i]], i]
            else:
                # 建立值和索引的关系
                dict[nums[i]] = i
# leetcode submit region end(Prohibit modification and deletion)


# 旧方案， 耗时久
#         length = len(nums)
#         for i in range(length-1):
#             for j in range(i+1,length):
#                 if nums[i]+nums[j] == target:
#                     res = [i,j]
#                     break
#         return res
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ] 
#  Related Topics 位运算 数组 回溯算法 
#  👍 807 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        if not nums:
            return result
        def generate(nums, index, result, tmp):

            if index == len(nums):
                # 不能直接append tmp
                result.append(tmp[:])
                return

            # 不添加nums[index]对应的元素
            generate(nums, index+1, result, tmp)
            # 添加nums[index]对应的元素到tmp列表里
            tmp.append(nums[index])
            generate(nums, index+1, result, tmp)
            # 更新tmp到前一状态
            tmp.pop()

        generate(nums, 0, result, [])

        return result


        # 迭代方案：
        # 对于[1,2,3] 过程为：
        # []
        # [] + [1]
        # [] [1] + [2] [1,2]
        # [] [1] [2] [1,2] + [3] [1,3] [2,3] [1,2,3]

        """
        # 迭代版本一
        result = [[]]
        # 遍历nums里的元素
        for num in nums:
            newsets = []
            for subset in result:
                new_subset = subset + [num]
                newsets.append(new_subset)
            result.extend(newsets)

        return result
        
        """

        """
        # 迭代版本2
        result = [[]]
        # 遍历nums里的元素
        for val in nums:
            result += [[val] + sub for sub in result]

        return result
        """
# leetcode submit region end(Prohibit modification and deletion)

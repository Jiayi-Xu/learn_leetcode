# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。 
# 
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
# 
#  请找出其中最小的元素。 
# 
#  你可以假设数组中不存在重复元素。 
# 
#  示例 1: 
# 
#  输入: [3,4,5,1,2]
# 输出: 1 
# 
#  示例 2: 
# 
#  输入: [4,5,6,7,0,1,2]
# 输出: 0 
#  Related Topics 数组 二分查找 
#  👍 266 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        while left < right:
            mid = (left + right)/2

            # 当nums[mid] < nums[mid-1]，则mid就是变化点，为最小值
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]

            # 从0-mid未发生旋转，为升序排列 继续往后查找
            if nums[mid] >= nums[0]:
                left = mid + 1
            # 从0-mid发生了旋转，需要往左查找
            if nums[mid] < nums[0]:
                right = mid


# leetcode submit region end(Prohibit modification and deletion)

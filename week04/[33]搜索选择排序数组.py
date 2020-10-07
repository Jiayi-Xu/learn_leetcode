# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。 
# 
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
# 
#  搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。 
# 
#  你可以假设数组中不存在重复的元素。 
# 
#  你的算法时间复杂度必须是 O(log n) 级别。 
# 
#  示例 1: 
# 
#  输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#  
# 
#  示例 2: 
# 
#  输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1 
#  Related Topics 数组 二分查找 
#  👍 992 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        left = 0
        right = len(nums) -1

        while left < right:
            mid = (left + right)/2
            # print("mid is", mid, nums[mid], "left is", left, "right is", right)
            # 当nums[0] < nums[mid], (0 - mid不包含旋转)，则从0～mid之间数值为递增
            # 如果target比nums[mid]还大或者比nums[0]还小，需要在右侧查找 例子：[4,5,6,7,0,1,2]
            if nums[0] <= nums[mid] and (nums[0] > target or target > nums[mid]):
                left = mid + 1
            # 当左侧非递增，说明0 - mid包含旋转，则从mid+1到最后一个数值为递增，且在nums[mid]~nums[0]之间
            # 需要在右侧查找 例子：[4,5,6,0,1,2,3]
            elif nums[0] > nums[mid] and nums[mid] < target and target < nums[0]:
                left = mid + 1
            # 其他情况，往前查找
            else:
                right = mid


        return left if left==right and nums[left] == target else -1
# leetcode submit region end(Prohibit modification and deletion)

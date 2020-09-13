# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。 
# 
#  示例 1: 
# 
#  输入: [1,2,3,4,5,6,7] 和 k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]
#  
# 
#  示例 2: 
# 
#  输入: [-1,-100,3,99] 和 k = 2
# 输出: [3,99,-1,-100]
# 解释: 
# 向右旋转 1 步: [99,-1,-100,3]
# 向右旋转 2 步: [3,99,-1,-100] 
# 
#  说明: 
# 
#  
#  尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。 
#  要求使用空间复杂度为 O(1) 的 原地 算法。 
#  
#  Related Topics 数组 
#  👍 690 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # 三次旋转
        # 当旋转数组 k 次， k%n个尾部元素会被移动到头部，剩下的元素会被向后移动。
        length = len(nums)
        k = k % length
        # 反转第一段，[4, 3, 2, 1, 5, 6, 7]
        # 反转第二段，[4, 3, 2, 1, 7, 6, 5]
        # 反转整体，[5, 6, 7, 1, 2, 3, 4]

        # 第一段 对应数组下标范围[0,n-k-1]
        nums[:length-k] = nums[:length-k][::-1]
        # 第二段，对应数组下标范围[n - k, n - 1]
        nums[length-k:] = nums[length-k:][::-1]
        nums[:] = nums[::-1]


# leetcode submit region end(Prohibit modification and deletion)

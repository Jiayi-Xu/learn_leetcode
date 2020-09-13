# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。 
# 
#  
# 
#  说明: 
# 
#  
#  初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。 
#  你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。 
#  
# 
#  
# 
#  示例: 
# 
#  输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6] 
#  Related Topics 数组 双指针 
#  👍 620 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # 暴力解法：将两个数组合并之后再排序
        # 使用双指针
        # p1指向nums1数组索引m-1；p2指向nums2数组索引n-1； p指向nums1数组最后一个索引
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # 当p1和p2没有指向数组第一个时候不断循环比较
        while p1>= 0 and p2>=0:
            # 第一个数组的元素大，则赋值给索引p位置，并且p1指针往前移动一格
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            # 第二个数组的元素大，则赋值给索引p位置，并且p2指针往前移动一格
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # 将剩余的nums2数组的元素赋值给nums1
        nums1[:p2+1] = nums2[:p2+1]
# leetcode submit region end(Prohibit modification and deletion)

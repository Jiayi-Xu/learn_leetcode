# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, 
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。 
# 
#  说明：你不能倾斜容器，且 n 的值至少为 2。 
# 
#  
# 
#  图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。 
# 
#  
# 
#  示例: 
# 
#  输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49 
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        i = 0
        j = len(height) - 1
        while i < j:
            maxArea = max(maxArea, (j - i) * min(height[i], height[j]))
            if height[i]>height[j]:
                # minHeight = height[j]
                j-=1
            else:
                # minHeight = height[i]
                i+=1
        return maxArea
# leetcode submit region end(Prohibit modification and deletion)

# listtest = [1,8,6,2,5,4,8,3,7]
#
# s1 = Solution()
# result = s1.maxArea(listtest)
# print(result)
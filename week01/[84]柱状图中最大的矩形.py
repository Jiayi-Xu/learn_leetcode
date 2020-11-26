# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  
# 
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。 
# 
#  
# 
#  
# 
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。 
# 
#  
# 
#  示例: 
# 
#  输入: [2,1,5,6,2,3]
# 输出: 10 
#  Related Topics 栈 数组 
#  👍 899 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        # """
        # 枚举左右边界 超时
        # """
        #
        # length = len(heights)
        # maxVal = 0
        # for i in xrange(length):
        #     minHeight = float("inf")
        #     for j in range(i,length):
        #         minHeight = min(minHeight, heights[j])
        #         maxVal = max(maxVal, (j-i+1)*minHeight)
        #
        # return maxVal

        """
        
        """
        new_len = len(heights) + 2
        newHeights = [0] * new_len
        newHeights[1:-1] = heights[:]

        maxArea = 0
        stack = [0]
        for i in range(1, new_len):
            while stack and newHeights[stack[-1]] > newHeights[i]:
                height = newHeights[stack.pop()]
                while stack and newHeights[stack[-1]] == height:
                    stack.pop()
                width = i - stack[-1] - 1 if stack else i
                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea

        """ 
        左边看一下，看最多能向左延伸多长，找到大于等于当前柱形高度的最左边元素的下标；
        右边看一下，看最多能向右延伸多长；找到大于等于当前柱形高度的最右边元素的下标。
        """

        
        # n = len(heights)
        # left, right = [0] * n, [n] * n
        #
        # mono_stack = list()
        # for i in range(n):
        #     while mono_stack and heights[mono_stack[-1]] >= heights[i]:
        #         right[mono_stack[-1]] = i
        #         mono_stack.pop()
        #     left[i] = mono_stack[-1] if mono_stack else -1
        #     mono_stack.append(i)
        #
        # ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        # return ans




# leetcode submit region end(Prohibit modification and deletion)

# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。 
# 
#  示例: 
# 
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6 
#  Related Topics 栈 数组 双指针 
#  👍 1646 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        ans = 0

        # 从左开始遍历
        for i in range(len(height)):
            # 当右边的柱子比左边高时候计算雨水面积
            while stack and height[i] > height[stack[-1]]:
                curIdx = stack[-1]
                # 如果栈顶元素一直相等，那么全都pop出去，只留第一个
                while stack and height[stack[-1]] == height[curIdx]:
                    stack.pop()

                if stack:
                    left = stack[-1]
                    right = i
                    h = min(height[left], height[right]) - height[curIdx]
                    w = right - left - 1
                    ans += w * h
            stack.append(i)

        return ans

# leetcode submit region end(Prohibit modification and deletion)

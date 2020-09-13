# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。 
# 
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。 
# 
#  你可以假设除了整数 0 之外，这个整数不会以零开头。 
# 
#  示例 1: 
# 
#  输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#  
# 
#  示例 2: 
# 
#  输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#  
#  Related Topics 数组 
#  👍 540 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 情况1：除 9之外的数字加一；
        # 情况2：数字 9 加一得10进一位 个位数为 0
        num = len(digits)
        for i in range(num-1, -1, -1):
            digits[i] += 1
            digits[i] = digits[i] % 10
            # 低位上非9，补偿后就直接返回。
            if digits[i] != 0:
                return digits

        new_digits = [0] * (num+1)
        # print("hello", new_digits)
        new_digits[0] = 1
        return new_digits
# leetcode submit region end(Prohibit modification and deletion)

# 执行耗时:12 ms,击败了97.38% 的Python用户
# 内存消耗:12.8 MB,击败了33.12% 的Python用户
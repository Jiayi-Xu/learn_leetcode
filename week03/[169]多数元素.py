# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。 
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [3,2,3]
# 输出: 3 
# 
#  示例 2: 
# 
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#  
#  Related Topics 位运算 数组 分治算法 
#  👍 745 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        或者排序后取下标为n/2的元素
        """
        # 使用dic存储元素出现次数
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1

        max_num = 0
        res = 0
        # 遍历dic 找次数最多的元素
        for k in dic:
            if dic[k] > max_num:
                max_num = dic[k]
                res = k
        return res
# leetcode submit region end(Prohibit modification and deletion)

# 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。 
# 
#  示例 1: 
# 
#  输入: 2
# 输出: [0,1,1] 
# 
#  示例 2: 
# 
#  输入: 5
# 输出: [0,1,1,2,1,2] 
# 
#  进阶: 
# 
#  
#  给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？ 
#  要求算法的空间复杂度为O(n)。 
#  你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。 
#  
#  Related Topics 位运算 动态规划 
#  👍 436 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        # 通过i&(i-1)消除最低位，剩余的数同样小于当前的i且已被计算过
        res = [0] * (num+1)
        for i in range(1,num+1):
            res[i] = res[i&(i-1)] + 1
        return res
# leetcode submit region end(Prohibit modification and deletion)

"""
        # 利用n&(n-1)计算1的数目
        res = []
        for i in range(num+1):
            count = 0
            while i:
                i = i & (i-1)
                count += 1
            res.append(count)
        return res
"""
"""
        res = []
        for i in range(num+1):
            res.append(bin(i).replace('0b','').count('1'))
        return res
"""
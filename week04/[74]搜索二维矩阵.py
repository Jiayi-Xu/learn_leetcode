# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  示例 1: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false 
#  Related Topics 数组 二分查找 
#  👍 254 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        """
        拉直后二分查找
        """

        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])

        length = row * col

        left = 0
        right = length - 1

        # if left == right:
        #     return matrix[left][right] == target

        while left < right:
            mid = (left + right)/2
            row_mid = mid / col
            col_mid = mid % col
            # print("row_mid",row_mid,"col_mid",col_mid)
            if matrix[row_mid][col_mid] < target:
                left = mid + 1
            elif matrix[row_mid][col_mid] > target:
                right = mid
            else:
                return True
            # print("left", left, "right", right)
        return left == right and matrix[left/col][left%col] == target

# leetcode submit region end(Prohibit modification and deletion)

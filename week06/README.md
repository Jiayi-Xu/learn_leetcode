## 学习笔记
 
+ 找到最近最简方法，将其拆解成可重复解决的问题
+ 数学归纳法思维
+ 动态规划：分治+最优子结构
	+ 共性：找到重复子问题
	+ 差异性：最优子结构，中途可以淘汰次优解
	+ 直接递归时间复杂度是指数级的
	+ DP步骤：a.重复性（分治） b.定义状态数组 c.DP方程

+ 斐波那契数列的计算方式：
	+ 自顶向下：记忆化搜索（memo数组）
	+ 自底向上：用for循环递推 a[i]=a[i-1]+a[i-2]


|#|标题|解决思路|
|---|---|------|
|53|[最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)|动态规划：max(0,nums[i-]) + nums[i]|
|62|[不同路径](https://leetcode-cn.com/problems/unique-paths/)|递归（自上而下）；动态规划（自下而上）|
|63|[不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)|动态规划（需要判断是否有障碍物）|
|120|[三角形最小路径和](https://leetcode-cn.com/problems/triangle/)|sub(i,j) = min(sub(i+1,j), sub(i+1,j+1)) + a[i,j]|
|1143|[最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)|动态规划|
||[]()||
||[]()||


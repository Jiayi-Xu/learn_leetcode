## 学习笔记
 

+ 递归
	+ 思维要点：
		+ 不要人肉进行递归
		+ 找最近重复子问题
		+ 数学归纳法思维 （例子放鞭炮）

	+ python模版：

````
def recursion(level, param1, param2, ...):
	# 终止循环条件
	if level > max_level:
		process_result
		return
	
	# 处理当前层
	process(level, data...)
	
	# 下探
	self.recursion(level+1, p1, ..)
	
	# 清扫当前层的状态
	
````
		


|#|标题|解决思路|
|---|---|------|
|22|[括号生成](https://leetcode-cn.com/problems/generate-parentheses/)|递归（设置left,right,n)|
|70|[爬楼梯](https://leetcode-cn.com/problems/two-sum/description/)| 递归（超时）；优化使用动态规划|
|98|[验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)|递归|
|104|[二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)|递归(返回左边的最大深度和右边的最大深度的最大值 +1)|
|111|[二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)|递归考虑三种情况；深度优先搜索:遍历整棵树，记录最小深度|

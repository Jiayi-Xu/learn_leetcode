## 学习笔记
 

+ DFS和BFS

````
def dfs(node):
	if node in visited:
		return
	
	visited.add(node)
	
	# 二叉树
	dfs(node.left)
	dfs(node.right)
````

````
visited = set()
def dfs(node, visited):
	# 为了严谨起见
	if node in visited:
		return
	visited.add(node)
	
	# 多叉树：把所有的children遍历
	for next_node in node.children():
		if not next_node in visited:
			dfs(next_node, visited)
````

+ DFS非递归写法

````
def DFS(tree):
	if tree.root is None:
		return []
	
	visited = []
	stack = [tree.root]
	
	while stack:
		node = stack.pop()
		visited.add(node)
		
		nodes = ...
		stack.push(nodes)
````

+ BFS非递归写法

````
def BFS(tree):
	if tree.root is None:
		return []
	
	visited = []
	queue = [tree.root]
	
	while queue:
		node = queue.pop(0)
		visited.add(node)
		
		nodes = ...
		queue.push(nodes)
````

+ 比较
	+ 贪心算法：当下做局部最优判断（例子：图中最小生成树，哈夫曼编码）
	+ 回溯：能够回退
	+ 动态规划：最优判断+回溯

+ 二分查找：单调，边界，index

|#|标题|解决思路|
|---|---|------|
|33|[搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)|二分查找|
|102|[二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/#/description)	||
|122|[买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/)|贪心算法|
|127|[单词接龙](https://leetcode-cn.com/problems/word-ladder/description/)|BFS|
|200|[岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)|DFS|
|455|[分发饼干](https://leetcode-cn.com/problems/assign-cookies/description/)|贪心算法|
|860|[柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/description/)|贪心算法|
|874|[模拟行走机器人](https://leetcode-cn.com/problems/walking-robot-simulation/description/)|dx,dy的处理|
||[]()||
||[]()||
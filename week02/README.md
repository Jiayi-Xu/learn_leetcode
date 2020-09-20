## 学习笔记
 

+ 四步法：
	+ clarification
	+ possible solutions->optimal(time & space)
	+ code
	+ test cases

+ 二叉搜索树（中序排列：为升序）
	+ 一颗空树或者具备下列性质的二叉树
	+ 左子树上 所有结点 的值均小于它的根结点的值
	+ 右子树上 所有结点 的值均大于它的根结点的值
	+ 类推左右子树也分别为二叉查找树 
+ 堆：
	+ 可以快速找到一堆数中的最大或最小值的数据结构



|#|标题|解决思路|
|---|---|------|
|1|[两数之和](https://leetcode-cn.com/problems/two-sum/description/)| for each a: check if target-a exists in nums; [hash解法遍历列表同时查字典](https://leetcode.com/problems/two-sum/discuss/96/HashtablePython5-lines)|
|49| [字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)||
|94|[二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)||
|242| [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/description/)| sort后再比较 $O(Nlog N)$; 使用Counter函数计算st字符数(但是时间复杂度高）|
|589| [N叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/)| 递归；迭代|
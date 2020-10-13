
## 题目



|编号|标题|解决思路|
|---|---|------|
|1|[两数之和](https://leetcode-cn.com/problems/two-sum/) | 哈希表：用字典存储值和索引位置的关系⭐️⭐️|
|11|[盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water) | 双指针（左右指针不断逼近）⭐️⭐️|
|15|[三数之和](https://leetcode-cn.com/problems/3sum)| 排序 + 双指针⭐️|
|17|[电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)	||
|21|[合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | 递归（确定好终止条件和循环条件）; 迭代（维护prehead）⭐️⭐️|
|22|[括号生成](https://leetcode-cn.com/problems/generate-parentheses/)|递归（设置left,right,n)|
|26|[删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | [双指针](https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/11751/Simple-Python-solution-O(n)) 指针i指向开始位置，指针j不断后移去找和i位置不同的值⭐️⭐️|
|42|[接雨水](https://leetcode-cn.com/problems/trapping-rain-water) | 维护一个单调栈⭐️|
|46|[全排列](https://leetcode-cn.com/problems/permutations/)|回溯 ⭐️⭐️|
|47|[全排列 II](https://leetcode-cn.com/problems/permutations-ii/)|比起46，需要多判断一步是否和之前添加过的元素重复|
|49|[字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)|使用defaultdict：sorted(str)作为key⭐️⭐️|
|剑指Offer 49| [丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)| |
|50|[Pow(x,n)](https://leetcode-cn.com/problems/powx-n/)|分治法|
|51|[N皇后](https://leetcode-cn.com/problems/n-queens/)|2|
|66|[加一](https://leetcode.com/problems/plus-one/) | 只有两种情况，除 9之外的数字加一；数字 9 加一得10进一位 个位数为 0 |
|70|[爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) | 递推，动态规划，每次只能爬 11 级或 22 级，所以 f(x)f(x) 只能从 f(x - 1)f(x−1) 和 f(x - 2)f(x−2) 转移过来|
|77|[组合](https://leetcode-cn.com/problems/combinations/)|回溯+剪枝|
|78|[子集](https://leetcode-cn.com/problems/subsets/)|类似括号题的思路，给n个格子，可选可不选|
|84|[柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram) | 栈|
|88|[合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) |使用了三个指针 p1指向num1数组位置m-1，p2指向num2数组位置n-1，p指针指向nums1数组最后一个位置|
|94|[二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)| 递归⭐️⭐️；迭代⭐️|
|98|[验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)|递归|
|104|[二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)|递归(返回左边的最大深度和右边的最大深度的最大值 +1)|
|105|[从前序和中序遍历构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)|前序遍历得到根结点位置，再划分左右结点不断遍历|
|111|[二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)|递归考虑三种情况；深度优先搜索:遍历整棵树，记录最小深度|
|144|[二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)| 递归⭐️⭐️；迭代⭐️|
|155|[最小栈](https://leetcode-cn.com/problems/min-stack) | getMin()函数实现再增加一个栈存储每次插入时候的最小值|
|169|[多数元素](https://leetcode-cn.com/problems/majority-element/description/)|哈希；排序取n/2|
|189|[旋转数组](https://leetcode-cn.com/problems/rotate-array) | 三次翻转k%n|
|206|[反转链表](https://leetcode-cn.com/problems/reverse-linked-list)|双指针|
|226| [翻转二叉树]()| 左右子树不断交换位置|
|236|[二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)||
|239|[滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum) | 双端队列|
|242| [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/description/)| sort后再比较 $O(Nlog N)$; 使用Counter函数计算st字符数(但是时间复杂度高）|
|283|[移动零](https://leetcode-cn.com/problems/move-zeroes)| 暴力：统计0的个数；用指针j存储非0元素的位置，遍历数组找不为0的值赋值给索引j对应的元素⭐️⭐️|
|429|[N叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)| 队列先进先出deque或者直接用list(queue),queue.pop[0] ⭐️⭐️ |
|589| [N叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/)| 递归；迭代stack倒插children节点⭐️⭐️|
|641|[设计循环双端队列](https://leetcode.com/problems/design-circular-deque/)| 需要capacity,size,front,rear,data参数，插入判断满，删除判断空|



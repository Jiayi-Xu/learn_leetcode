
## 题目



|#|标题|解决思路|
|---|---|------|
|1|[两数之和](https://leetcode-cn.com/problems/two-sum/) | 哈希表：用字典存储值和索引位置的关系⭐️⭐️|
|11|[盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water) | 双指针（左右指针不断逼近）⭐️⭐️|
|15|[三数之和](https://leetcode-cn.com/problems/3sum)| 排序 + 双指针⭐️|
|21|[合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | 递归（确定好终止条件和循环条件）; 迭代（维护prehead）⭐️⭐️|
|26|[删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | [双指针](https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/11751/Simple-Python-solution-O(n)) 指针i指向开始位置，指针j不断后移去找和i位置不同的值⭐️⭐️|
|42|[接雨水](https://leetcode-cn.com/problems/trapping-rain-water) | 维护一个单调栈⭐️|
|49|[字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)|使用defaultdict：sorted(str)作为key|
|剑指Offer 49| [丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)| |
|66|[加一](https://leetcode.com/problems/plus-one/) | 只有两种情况，除 9之外的数字加一；数字 9 加一得10进一位 个位数为 0 |
|70|[爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) | 递推，动态规划，每次只能爬 11 级或 22 级，所以 f(x)f(x) 只能从 f(x - 1)f(x−1) 和 f(x - 2)f(x−2) 转移过来|
|84|[柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram) | 栈|
|88|[合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) |使用了三个指针 p1指向num1数组位置m-1，p2指向num2数组位置n-1，p指针指向nums1数组最后一个位置|
|94|[二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)| 递归；迭代|
|144|[二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)| 递归；迭代|
|155|[最小栈](https://leetcode-cn.com/problems/min-stack) | getMin()函数实现再增加一个栈存储每次插入时候的最小值|
|189|[旋转数组](https://leetcode-cn.com/problems/rotate-array) | 三次翻转k%n|
|206|[反转链表](https://leetcode-cn.com/problems/reverse-linked-list)|双指针|
|239|[滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum) | 双端队列|
|242| [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/description/)| sort后再比较 $O(Nlog N)$; 使用Counter函数计算st字符数(但是时间复杂度高）|
|283|[移动零](https://leetcode-cn.com/problems/move-zeroes)| 暴力：统计0的个数；用指针j存储非0元素的位置，遍历数组找不为0的值赋值给索引j对应的元素⭐️⭐️|
|429|[N叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)| 队列先进先出deque|
|589| [N叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/)| 递归；迭代|
|641|[设计循环双端队列](https://leetcode.com/problems/design-circular-deque/)| 需要capacity,size,front,rear,data参数，插入判断满，删除判断空|



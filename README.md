
## 题目



|编号|标题|解决思路|时间复杂度|
|---|---|------|---|
|1|[两数之和](https://leetcode-cn.com/problems/two-sum/) | 哈希表：用字典存储值和索引位置的关系⭐️⭐️|
|2|[两数相加](https://leetcode-cn.com/problems/add-two-numbers/)|返回的是链表，设置d和p指向头指针，p不断更新，最后返回d.next|O(n)|
|11|[盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water) | 枚举($O(n^2)$); 双指针（左右指针不断逼近）|O(n)|
|15|[三数之和](https://leetcode-cn.com/problems/3sum)| 排序 + 双指针(当nums[i+1]==nums[i]时候需要再移动，判重)|暴力$O(n^3)$|
|17|[电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)	||
|20|[有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)|栈⭐️|
|21|[合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | 递归（确定好终止条件和循环条件）; 迭代（维护prehead）⭐️⭐️|
|22|[括号生成](https://leetcode-cn.com/problems/generate-parentheses/)|递归（设置left,right,n)|
|26|[删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | [双指针](https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/11751/Simple-Python-solution-O(n)) 指针i指向开始位置，指针j不断后移去找和i位置不同的值⭐️⭐️|
|32|[最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)|动态规划；栈|
|33|[搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)|二分查找|
|42|[接雨水](https://leetcode-cn.com/problems/trapping-rain-water) | 维护一个单调栈⭐️|
|46|[全排列](https://leetcode-cn.com/problems/permutations/)|回溯 ⭐️⭐️|
|47|[全排列 II](https://leetcode-cn.com/problems/permutations-ii/)|比起46，需要多判断一步是否和之前添加过的元素重复⭐️⭐️|
|49|[字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)|使用defaultdict：sorted(str)作为key⭐️⭐️|
|剑指Offer 49| [丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)| |
|50|[Pow(x,n)](https://leetcode-cn.com/problems/powx-n/)|分治法|
|51|[N皇后](https://leetcode-cn.com/problems/n-queens/)||
|53|[最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)|动态规划：max(0,nums[i-]) + nums[i]|
|55|[跳跃游戏](https://leetcode-cn.com/problems/jump-game/)|贪心算法|
|62|[不同路径](https://leetcode-cn.com/problems/unique-paths/)|递归（自上而下）；动态规划（自下而上）|
|63|[不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)|动态规划（需要判断是否有障碍物）|
|64|[最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)|动态规划dp[i][j] = min(dp[i-1][j], dp[i][j-1])|
|66|[加一](https://leetcode.com/problems/plus-one/) | 只有两种情况，除 9之外的数字加一；数字 9 加一得10进一位 个位数为 0 |
|70|[爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) | 递推，动态规划，每次只能爬 1级或 2级，所以 f(x) 只能从 f(x - 1)和 f(x - 2)转移过来|O(n)|
|72|[编辑距离](https://leetcode-cn.com/problems/edit-distance/)|动态规划：二维数组，替换操作 = dp[i - 1][j - 1] + 1，删除操作 = dp[i - 1][j] + 1，增加操作 = dp[i][j - 1] + 1|
|74|[搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)|拉直后进行二分查找，再转换对应的row和col|
|77|[组合](https://leetcode-cn.com/problems/combinations/)|回溯+剪枝|
|78|[子集](https://leetcode-cn.com/problems/subsets/)|类似括号题的思路，给n个格子，可选可不选|
|84|[柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram) | 栈(哨兵)，固定高度找width| 时间空间复杂度O(n)⭐️⭐️⭐️⭐️|
|88|[合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) |使用了三个指针 p1指向num1数组位置m-1，p2指向num2数组位置n-1，p指针指向nums1数组最后一个位置|
|91|[解码方法](https://leetcode-cn.com/problems/decode-ways/)||
|94|[二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)| 递归⭐️⭐️；迭代⭐️|
|98|[验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)|递归|
|102|[二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/#/description)	|使用queue做⭐️⭐️|
|104|[二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)|递归(返回左边的最大深度和右边的最大深度的最大值 +1)|
|105|[从前序和中序遍历构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)|前序遍历得到根结点位置，再划分左右结点不断遍历|
|111|[二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)|递归考虑三种情况；深度优先搜索:遍历整棵树，记录最小深度|
|120|[三角形最小路径和](https://leetcode-cn.com/problems/triangle/)|sub(i,j) = min(sub(i+1,j), sub(i+1,j+1)) + a[i,j]|
|122|[买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/description/)|贪心算法⭐️⭐️|
|127|[单词接龙](https://leetcode-cn.com/problems/word-ladder/description/)|BFS|
|141|[环形链表](https://leetcode.com/problems/linked-list-cycle/)|哈希表时间空间复杂度都为O(n); 快慢指针（时间复杂度O(n),空间复杂度O(1)||
|144|[二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)| 递归⭐️⭐️；迭代⭐️|
|146|[LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/)|使用OrderedDict, popitem(last=False)时删除第一个键值对|
|153|[寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)|二分查找，找变化点|
|155|[最小栈](https://leetcode-cn.com/problems/min-stack) | getMin()函数实现再增加一个栈存储每次插入时候的最小值min_stack||
|169|[多数元素](https://leetcode-cn.com/problems/majority-element/description/)|哈希；排序取n/2|
|189|[旋转数组](https://leetcode-cn.com/problems/rotate-array) | 三次翻转k%n|
|198|[打家劫舍](https://leetcode-cn.com/problems/house-robber/)|动态规划：【不偷a[i][0]】 a[i][0] = max(a[i-1][0], a[i-1][1]) 【偷a[i][1]】 a[i][1] = a[i-1][0] + nums[i] |
|200|[岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)|DFS|
|206|[反转链表](https://leetcode-cn.com/problems/reverse-linked-list)|双指针|
|221|[最大正方形](https://leetcode-cn.com/problems/maximal-square/)|动态规划，dp[i][j]代表右下角，由它的左，上，斜对角过渡过来|
|222|[完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes/)|递归；||
|226| [翻转二叉树]()| 左右子树不断交换位置|
|236|[二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)||
|237|[删除链表中的节点](https://leetcode-cn.com/problems/delete-node-in-a-linked-list/)|不能得到node前一个节点的信息，但是可以通过将下一个节点的值赋给node，再把node下一个节点删除，效果一样||
|239|[滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum) | 双端队列|
|242| [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/description/)| sort后再比较 $O(Nlog N)$; 使用Counter函数计算st字符数(但是时间复杂度高）|
|283|[移动零](https://leetcode-cn.com/problems/move-zeroes)| 暴力：统计0的个数；用指针j存储非0元素的位置，遍历数组找不为0的值赋值给索引j对应的元素|O(n)|
|290|[单词规律](https://leetcode-cn.com/problems/word-pattern/)|各自映射到新的编码再进行比较|
|387|[字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)|hashmap|
|389|[找不同](https://leetcode-cn.com/problems/find-the-difference/)|字符串ASCII差值，异或法|
|394|[字符串解码](https://leetcode-cn.com/problems/decode-string/)||
|429|[N叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)| 队列先进先出deque或者直接用list(queue),queue.pop[0] ⭐️⭐️ |
|452|[用最少数量的箭引爆气球](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/)|时间复杂度：O(nlog n),排序的时间复杂度为 O(nlog n)，对所有气球进行遍历并计算答案的时间复杂度为 O(n)|时间复杂度O(nlog n) 空间复杂度O(log n)（因为排序）|
|455|[分发饼干](https://leetcode-cn.com/problems/assign-cookies/description/)|贪心算法⭐️⭐️|
|529|[扫雷游戏](https://leetcode-cn.com/problems/minesweeper/)||
|589| [N叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/)| 递归；迭代stack倒插children节点⭐️⭐️|
|641|[设计循环双端队列](https://leetcode.com/problems/design-circular-deque/)| 需要capacity,size,front,rear,data参数，插入判断满，删除判断空|
|647|[回文子串](https://leetcode-cn.com/problems/palindromic-substrings/)|动态规划：分1，2，大于2个字符的比较|
|860|[柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/description/)|贪心算法⭐️⭐️|
|874|[模拟行走机器人](https://leetcode-cn.com/problems/walking-robot-simulation/description/)|dx,dy的处理|
|1143|[最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)|动态规划|
|1370|[上升下降字符串](https://leetcode-cn.com/problems/increasing-decreasing-string/)|设置26个计数桶|O(n)|



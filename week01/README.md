## 学习笔记
 

+ 1.看题5-10分钟，如果没有思路，看题解，不要死磕
+ 2.五毒神掌，需要去过遍数； 
+ 3.看题解先看cn版再看国际vote票数高的几篇

#### 快慢指针题目需要多练习


|#|标题|解决思路|
|---|---|------|
|70|[爬楼梯](https://leetcode-cn.com/problems/climbing-stairs) | 递推，动态规划，每次只能爬 11 级或 22 级，所以 f(x)f(x) 只能从 f(x - 1)f(x−1) 和 f(x - 2)f(x−2) 转移过来|
|11|[盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water) | 双指针（左右指针不断逼近）|
|283|[移动零](https://leetcode-cn.com/problems/move-zeroes)| 暴力：统计0的个数, 用指针j存储非0元素的位置|
|15|[三数之和](https://leetcode-cn.com/problems/3sum)| 排序 + 双指针|
|206|[反转链表](https://leetcode-cn.com/problems/reverse-linked-list)|双指针|
|21|[合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists) | 递归（确定好终止条件和循环条件）|
|155|[最小栈](https://leetcode-cn.com/problems/min-stack) | getMin()函数实现再增加一个栈存储每次插入时候的最小值|
|84|[柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram) | 栈|
|239|[滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum) | 双端队列|
|42|[接雨水](https://leetcode-cn.com/problems/trapping-rain-water) | 栈|
|26|[删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) | 快慢指针|
|189|[旋转数组](https://leetcode-cn.com/problems/rotate-array) | 三次翻转k%n|
|88|[合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array) |使用了三个指针|
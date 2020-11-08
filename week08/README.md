## week8学习笔记
 
+ N皇后2 位运算代码：https://shimo.im/docs/YzWa5ZZrZPYWahK2/read
	+ 用位运算记录皇后的信息，可以将记录皇后信息的空间复杂度从 O(N)降到 O(1)。

+ 布隆过滤器：Bloom Filter 和哈希表类似
	+ 一个很长的二进制向量和一系列随机映射函数，用于检索一个元素是否在一个集合中，空间效率和查询时间远超一般的算法
	+ 比较：哈希表能存其它冗余信息，但布隆过滤器只能查询不能存储其他额外信息，且有一定误识别率和删除困难
	+ 案例：比特币网络，分布式系统，redis缓存，垃圾邮件评论的过滤（如果查到再进db查，没查到就肯定没有，直接略过）

+ LRU替换策略：
	+ LRU: least recently used
	+ LFU: least frequently used 


+ 排序算法：
	+ 比较类排序：通过比较来决定元素间的相对顺序（非线性时间比较类排序）
	+ 非比较类排序：可以突破基于比较排序的时间下界，以线性时间运行



|#|标题|解决思路|
|---|---|------|
|51|[N皇后](https://leetcode-cn.com/problems/n-queens/description/)|dfs|
|52|[N皇后 II](https://leetcode-cn.com/problems/n-queens-ii/description/)|位运算|
|146|[LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/#/)|使用OrderedDict|
|190|[颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/)|n&1判断最后一位，不断左移|
|191|[位1的个数](https://leetcode-cn.com/problems/number-of-1-bits/)|n&(n-1)|
|231|[2的幂](https://leetcode-cn.com/problems/power-of-two/)|n&(n-1)|
|338|[比特位计数](https://leetcode-cn.com/problems/counting-bits/)|位运算+动态规划：n&(n-1)消除最低位，补上1，剩余的数小于当前值（之前已计算过）|
||[]()||
||[]()||
||[]()||
||[]()||

![](pic/排序.png)

![](pic/时间复杂度.png)
## week8学习笔记
 
+ N皇后2 位运算代码：https://shimo.im/docs/YzWa5ZZrZPYWahK2/read
	+ 用位运算记录皇后的信息，可以将记录皇后信息的空间复杂度从 O(N)降到 O(1)。

+ 布隆过滤器：Bloom Filter 和哈希表类似
	+  

|#|标题|解决思路|
|---|---|------|
|51|[N皇后](https://leetcode-cn.com/problems/n-queens/description/)|dfs|
|52|[N皇后 II](https://leetcode-cn.com/problems/n-queens-ii/description/)|位运算|
|190|[颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/)|n&1判断最后一位，不断左移|
|191|[位1的个数](https://leetcode-cn.com/problems/number-of-1-bits/)|n&(n-1)|
|231|[2的幂](https://leetcode-cn.com/problems/power-of-two/)|n&(n-1)|
|338|[比特位计数](https://leetcode-cn.com/problems/counting-bits/)|位运算+动态规划：n&(n-1)消除最低位，补上1，剩余的数小于当前值（之前已计算过）|
||[]()||
||[]()||
||[]()||
||[]()||


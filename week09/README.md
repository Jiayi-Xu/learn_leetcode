## week9学习笔记
 
+ 最长子序列：

````
if s[i-1] == s[j-1]:
	dp[i][j] = dp[i-1][j-1] + 1 # 因为i,j都被占用
else:
	dp[i][j] = max(dp[i-1][j], dp[i][j-1])
````

+ 最长子串

````
if s[i-1] == s[j-1]:
	dp[i][j] = dp[i-1][j-1] + 1
else:
	dp[i][j] = 0 # 没有公共子串
````

+ 字符
	+ 'A' - 'Z' 对应的 ascii 是 65 - 90
	+ 'a' - 'z' 对应的 ascii 是 97 - 122
+ 回文
	+ 回文串一定是对称的，可以循环选择一个中心，进行左右扩展，判断左右字符是否相等
	+ 因为回文串可以是奇数和偶数长度，扩展时候要按字符扩展和两个字符之间扩展，所以中心点有N+(N-1)个

+ 字符串匹配算法
	+ 暴力：时间复杂度O(mn) 
	+ KMP: 找已经匹配的片段，它的最大的前缀和最大的后缀最长有多长

|#|标题|解决思路|
|---|---|------|
|151|[翻转字符串里的单词](https://leetcode-cn.com/problems/reverse-words-in-a-string/)||
|387|[字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)|hashmap|
|541|[反转字符串 II](https://leetcode-cn.com/problems/reverse-string-ii/)||
|557|[反转字符串中的单词 III](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/)||
|709|[转换成小写字母](https://leetcode-cn.com/problems/to-lower-case/)|ord/chr|
|917|[仅仅反转字母](https://leetcode-cn.com/problems/reverse-only-letters/)|双指针；使用栈存字母|
||[]()||
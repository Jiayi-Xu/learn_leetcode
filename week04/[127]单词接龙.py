# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：
#  
# 
#  
#  每次转换只能改变一个字母。 
#  转换过程中的中间单词必须是字典中的单词。 
#  
# 
#  说明: 
# 
#  
#  如果不存在这样的转换序列，返回 0。 
#  所有单词具有相同的长度。 
#  所有单词只由小写字母组成。 
#  字典中不存在重复的单词。 
#  你可以假设 beginWord 和 endWord 是非空的，且二者不相同。 
#  
# 
#  示例 1: 
# 
#  输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# 
# 输出: 5
# 
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
#      返回它的长度 5。
#  
# 
#  示例 2: 
# 
#  输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# 
# 输出: 0
# 
# 解释: endWord "cog" 不在字典中，所以无法进行转换。 
#  Related Topics 广度优先搜索 
#  👍 465 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        # BFS
        queue = [beginWord]
        visited = set(beginWord)
        word_len = len(beginWord)

        # 建立无向图
        combination = defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                combination[word[:i] + "*" + word[i + 1:]].append(word)


        step = 1

        while queue:
            tmp_size = len(queue)

            for i in range(tmp_size):
                word = queue.pop(0)

                for j in range(word_len):
                    key_relation = word[:j] + "*" + word[j+1:]
                    # print(key_relation)
                    for next_word in combination[key_relation]:
                        # print(next_word)
                        if next_word not in visited:
                            # 将这个词添加到队列里
                            queue.append(next_word)
                            visited.add(next_word)
                            if next_word == endWord:
                                return step + 1

            step += 1

        return 0







# leetcode submit region end(Prohibit modification and deletion)
